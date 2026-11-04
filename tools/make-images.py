"""
Image preparation for the River Valley Robotics site.

Uses the team's own Instagram photos in source/instagram. Run from the
project root:

    python tools/make-images.py

Outputs compressed .webp files in assets/img and a social sharing card.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"
SRC = ROOT / "source" / "instagram"


def load(path):
    return Image.open(path).convert("RGB")


def cover_crop(image, width, height, focus_x=0.5, focus_y=0.5):
    """Crop to the target aspect ratio, then resize to width x height."""
    src_ratio = image.width / image.height
    target_ratio = width / height
    if src_ratio > target_ratio:
        crop_w = int(image.height * target_ratio)
        left = int((image.width - crop_w) * focus_x)
        box = (left, 0, left + crop_w, image.height)
    else:
        crop_h = int(image.width / target_ratio)
        top = int((image.height - crop_h) * focus_y)
        box = (0, top, image.width, top + crop_h)
    return image.crop(box).resize((width, height), Image.LANCZOS)


def save_webp(image, name, quality=82):
    out = IMG / name
    image.save(out, "WEBP", quality=quality, method=6)
    print(f"wrote {out.relative_to(ROOT)}  {image.width}x{image.height}  {out.stat().st_size // 1024} KB")


def main():
    IMG.mkdir(parents=True, exist_ok=True)

    shop = load(SRC / "shop-bench.jpg")
    save_webp(cover_crop(shop, 1400, 933, 0.5, 0.58), "team-shop-hero.webp", 84)
    save_webp(cover_crop(shop, 1100, 1100, 0.5, 0.5), "team-shop.webp", 83)
    save_webp(cover_crop(shop, 1000, 1250, 0.5, 0.5), "team-shop-portrait.webp", 82)

    students = load(SRC / "students-workshop.jpg")
    save_webp(cover_crop(students, 1000, 1250, 0.5, 0.45), "students-workshop.webp", 83)
    save_webp(cover_crop(students, 1200, 900, 0.5, 0.32), "students-workshop-wide.webp", 83)

    robot = load(SRC / "robot-floor.jpg")
    save_webp(cover_crop(robot, 1000, 1250, 0.5, 0.55), "robot-floor.webp", 83)

    photos = [
        ("student-desk.jpg", "student-desk.webp", 0.5, 0.5),
        ("electronics-bench.jpg", "electronics-bench.webp", 0.5, 0.5),
        ("parts-homework.jpg", "parts-homework.webp", 0.5, 0.5),
        ("soldering-arm.jpg", "soldering-arm.webp", 0.5, 0.5),
        ("soldering-closeup.jpg", "soldering-closeup.webp", 0.5, 0.5),
        ("chassis-electronics.jpg", "chassis-electronics.webp", 0.5, 0.5),
        ("armor-part.jpg", "armor-part.webp", 0.5, 0.5),
        ("cad-chassis.jpg", "cad-chassis.webp", 0.5, 0.5),
        ("cad-chassis-top.jpg", "cad-chassis-top.webp", 0.5, 0.5),
    ]
    for source, output, fx, fy in photos:
        save_webp(cover_crop(load(SRC / source), 1000, 1250, fx, fy), output, 82)

    flyer = load(SRC / "2025-first-meeting-flyer.jpg")
    save_webp(flyer.resize((1000, int(flyer.height * 1000 / flyer.width)), Image.LANCZOS), "meeting-flyer.webp", 86)

    update = load(SRC / "2026-club-update-flyer.jpg")
    save_webp(update.resize((1000, int(update.height * 1000 / update.width)), Image.LANCZOS), "club-update.webp", 86)

    # Smaller JPEGs keep the printed sponsorship packet light enough to email.
    packet_images = [
        (robot, "packet-robot.jpg", 0.45, 0.55),
        (load(SRC / "cad-chassis-top.jpg"), "packet-cad.jpg", 0.5, 0.5),
        (load(SRC / "soldering-arm.jpg"), "packet-soldering.jpg", 0.5, 0.5),
    ]
    for image, name, fx, fy in packet_images:
        out = cover_crop(image, 720, 900, fx, fy)
        path = IMG / name
        out.save(path, "JPEG", quality=82, optimize=True)
        print(f"wrote {path.relative_to(ROOT)}  {out.width}x{out.height}  {path.stat().st_size // 1024} KB")

    # Social sharing card
    green = (23, 61, 32)
    green_light = (143, 202, 159)
    silver = (201, 208, 204)
    og = Image.new("RGB", (1200, 630), green)
    photo = cover_crop(robot, 540, 630, 0.45, 0.55)
    og.paste(photo, (660, 0))
    overlay = Image.new("RGBA", (540, 630), (0, 0, 0, 0))
    for x in range(540):
        alpha = max(0, int(235 * (1 - x / 310)))
        ImageDraw.Draw(overlay).line((x, 0, x, 630), fill=(*green, alpha))
    og.paste(overlay, (660, 0), overlay)

    logo = Image.open(ROOT / "source" / "logo-full.png").convert("RGBA")
    logo.thumbnail((260, 260), Image.LANCZOS)
    og.paste(logo, (64, 54), logo)

    draw = ImageDraw.Draw(og)
    font_bold = str(ROOT / "source" / "fonts" / "BarlowCondensed-Bold.ttf")
    font_semi = str(ROOT / "source" / "fonts" / "BarlowCondensed-SemiBold.ttf")
    draw.rectangle((64, 342, 164, 348), fill=green_light)
    draw.text((62, 372), "RIVER VALLEY", font=ImageFont.truetype(font_bold, 54), fill=(255, 255, 255))
    draw.text((62, 420), "ROBOTICS", font=ImageFont.truetype(font_bold, 96), fill=green_light)
    draw.text((64, 536), "COMBAT ROBOTICS  /  YUBA CITY, CA", font=ImageFont.truetype(font_semi, 21), fill=silver)
    draw.text((64, 566), "rvrobotics.ycusd.org", font=ImageFont.truetype(font_semi, 21), fill=(255, 255, 255))
    og.save(IMG / "og.jpg", "JPEG", quality=88, optimize=True)
    print("wrote assets/img/og.jpg")


if __name__ == "__main__":
    main()
