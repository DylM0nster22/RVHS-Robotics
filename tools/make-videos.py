"""
Prepare match videos and poster cards for the Watch page.

The web-ready MP4s and poster images are committed with the site, so a normal
build does not need ffmpeg. Run this only when new match footage arrives.

Usage (from the project root):

    $env:FFMPEG = "C:\\path\\to\\ffmpeg.exe"
    python tools/make-videos.py --source "D:\\path\\to\\match-footage"

Outputs:
    assets/video/<slug>.mp4          web-optimized 720p match video
    assets/img/video/<slug>.webp     poster frame
    assets/img/video/yt-<slug>.webp  poster for a YouTube pick

Use --youtube to refresh the YouTube thumbnails as well. Use --force to
re-encode videos that already exist.
"""

import argparse
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

from pages.watch import FEATURED, LOCAL_VIDEOS, YOUTUBE_VIDEOS  # noqa: E402

VIDEO_OUT = ROOT / "assets" / "video"
POSTER_OUT = ROOT / "assets" / "img" / "video"
FONT_SEMI = ROOT / "source" / "fonts" / "BarlowCondensed-SemiBold.ttf"

WIDTH = 1280
HEIGHT = 720


def find_ffmpeg(explicit):
    if explicit:
        return explicit
    import os

    if os.environ.get("FFMPEG"):
        return os.environ["FFMPEG"]
    found = shutil.which("ffmpeg")
    if found:
        return found
    raise SystemExit(
        "ffmpeg was not found. Put it on PATH, set the FFMPEG environment "
        "variable, or pass --ffmpeg."
    )


def run(command):
    subprocess.run(command, check=True)


def probe_duration(ffmpeg, path):
    result = subprocess.run(
        [ffmpeg, "-hide_banner", "-i", str(path)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    match = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", result.stderr)
    if not match:
        raise SystemExit(f"Could not read the duration of {path}")
    hours, minutes, seconds = match.groups()
    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


def extract_frame(ffmpeg, source, destination, at_seconds):
    run(
        [
            ffmpeg,
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            f"{at_seconds:.2f}",
            "-i",
            str(source),
            "-frames:v",
            "1",
            "-q:v",
            "2",
            "-y",
            str(destination),
        ]
    )


def write_poster(frame_path, output_path):
    image = Image.open(frame_path).convert("RGB")
    # The event recording burns a large timer and channel mark into the top of
    # every frame. Crop that strip out so the card shows footage, not a clock.
    top = 112
    image = image.crop((0, top, WIDTH, HEIGHT))
    target_width = int(round(image.height * 16 / 9))
    left = (image.width - target_width) // 2
    image = image.crop((left, 0, left + target_width, image.height))
    image = image.resize((WIDTH, HEIGHT), Image.LANCZOS)

    shade = Image.new("RGBA", image.size, (0, 0, 0, 0))
    shade_draw = ImageDraw.Draw(shade)
    for y in range(320, HEIGHT):
        amount = (y - 320) / (HEIGHT - 320)
        alpha = int(218 * (amount ** 1.4))
        shade_draw.line((0, y, WIDTH, y), fill=(8, 13, 10, alpha))
    image = Image.alpha_composite(image.convert("RGBA"), shade).convert("RGB")

    # Cover the event channel's bottom-left bug with a small team wordmark.
    corner = Image.new("RGBA", image.size, (0, 0, 0, 0))
    corner_draw = ImageDraw.Draw(corner)
    corner_draw.polygon([(0, 610), (245, 610), (325, 720), (0, 720)], fill=(9, 14, 11, 242))
    image = Image.alpha_composite(image.convert("RGBA"), corner).convert("RGB")

    draw = ImageDraw.Draw(image)
    draw.rectangle((44, 652, 84, 655), fill=(143, 202, 159))
    wordmark = ImageFont.truetype(str(FONT_SEMI), 21)
    draw.text((44, 664), "RIVER VALLEY ROBOTICS", font=wordmark, fill=(214, 222, 216))

    image.save(output_path, "WEBP", quality=84, method=6)
    print(f"  poster {output_path.relative_to(ROOT)}  ({output_path.stat().st_size // 1024} KB)")


def encode_video(ffmpeg, source, output):
    run(
        [
            ffmpeg,
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(source),
            "-vf",
            f"scale={WIDTH}:{HEIGHT}:flags=lanczos",
            "-c:v",
            "libx264",
            "-preset",
            "slow",
            "-crf",
            "30",
            "-profile:v",
            "high",
            "-level",
            "3.1",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "64k",
            "-ac",
            "1",
            "-movflags",
            "+faststart",
            "-map_metadata",
            "-1",
            "-y",
            str(output),
        ]
    )
    print(f"  video  {output.relative_to(ROOT)}  ({output.stat().st_size // (1024 * 1024)} MB)")


def download_youtube_poster(video, output_path):
    last_error = None
    for name in ("maxresdefault", "sddefault", "hqdefault"):
        url = f"https://i.ytimg.com/vi/{video['id']}/{name}.jpg"
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                data = response.read()
        except Exception as error:  # noqa: BLE001 - fall back to the next size
            last_error = error
            continue

        temp = POSTER_OUT / f".{video['slug']}.jpg"
        temp.write_bytes(data)
        try:
            image = Image.open(temp).convert("RGB")
            image = ImageOps.fit(image, (WIDTH, HEIGHT), method=Image.LANCZOS)
            if image.width < 900:
                image = image.filter(ImageFilter.UnsharpMask(radius=1.2, percent=70, threshold=3))
            image.save(output_path, "WEBP", quality=84, method=6)
        finally:
            temp.unlink(missing_ok=True)
        print(f"  poster {output_path.relative_to(ROOT)}  ({output_path.stat().st_size // 1024} KB)")
        return

    print(f"  skipped YouTube poster for {video['id']}: {last_error}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source",
        type=Path,
        default=ROOT / "source" / "videos",
        help="Folder containing the original match MP4s.",
    )
    parser.add_argument("--ffmpeg", help="Path to ffmpeg.exe.")
    parser.add_argument("--force", action="store_true", help="Re-encode videos that already exist.")
    parser.add_argument("--youtube", action="store_true", help="Refresh YouTube thumbnail images.")
    parser.add_argument("--skip-video", action="store_true", help="Only rebuild posters.")
    args = parser.parse_args()

    ffmpeg = find_ffmpeg(args.ffmpeg)
    if not args.source.is_dir():
        raise SystemExit(f"Video source folder not found: {args.source}")

    VIDEO_OUT.mkdir(parents=True, exist_ok=True)
    POSTER_OUT.mkdir(parents=True, exist_ok=True)

    for video in LOCAL_VIDEOS:
        source = args.source / video["source"]
        if not source.is_file():
            raise SystemExit(f"Missing source video: {source}")

        slug = video["slug"]
        output_video = VIDEO_OUT / f"{slug}.mp4"
        output_poster = POSTER_OUT / f"{slug}.webp"

        print(f"{source.name}")
        if not args.skip_video and (args.force or not output_video.is_file() or output_video.stat().st_mtime < source.stat().st_mtime):
            encode_video(ffmpeg, source, output_video)
        else:
            print(f"  video  {output_video.relative_to(ROOT)} (kept)")

        duration = probe_duration(ffmpeg, source)
        at_seconds = max(2.0, min(duration - 2.0, duration * 0.5))
        frame = POSTER_OUT / f".{slug}-frame.jpg"
        extract_frame(ffmpeg, source, frame, at_seconds)
        try:
            write_poster(frame, output_poster)
        finally:
            frame.unlink(missing_ok=True)

    if args.youtube:
        print("YouTube posters")
        for video in YOUTUBE_VIDEOS:
            download_youtube_poster(video, POSTER_OUT / f"yt-{video['slug']}.webp")

    featured_poster = POSTER_OUT / f"{FEATURED}.webp"
    if featured_poster.is_file():
        print(f"\nFeatured poster: {featured_poster.relative_to(ROOT)}")
    print("Done.")


if __name__ == "__main__":
    main()
