"""
Image preparation for the River Valley Robotics site.

Uses the team's own Instagram photos (assets/img/instagram). Run from the
project root:
    python tools/make-images.py

Outputs compressed .webp files in assets/img and a social sharing card.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFont

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

    shop = load(SRC / "DfOeaWllCbb_3_1167x1556.jpg")
    # Landscape crop through the middle of the workbench for the hero.
    save_webp(cover_crop(shop, 1400, 933, 0.5, 0.58), "team-shop-hero.webp", 84)
    save_webp(cover_crop(shop, 1100, 1100, 0.5, 0.5), "team-shop.webp", 83)
    save_webp(cover_crop(shop, 1000, 1250, 0.5, 0.5), "team-shop-portrait.webp", 82)

    flyer = load(SRC / "DO43grQkdZL_1_1182x1574.jpg")
    save_webp(flyer.resize((1000, int(flyer.height * 1000 / flyer.width)), Image.LANCZOS), "meeting-flyer.webp", 86)

    update = load(SRC / "DfOeaWllCbb_1_1182x1576.jpg")
    save_webp(update.resize((1000, int(update.height * 1000 / update.width)), Image.LANCZOS), "club-update.webp", 86)

    # Social sharing card
    og = Image.new("RGB", (1200, 630), (246, 243, 234))
    draw = ImageDraw.Draw(og)
    for x in range(0, 1200, 40):
        draw.line((x, 0, x, 630), fill=(233, 228, 217), width=1)
    for y in range(0, 630, 40):
        draw.line((0, y, 1200, y), fill=(233, 228, 217), width=1)
    draw.rectangle((0, 0, 1200, 12), fill=(11, 58, 35))
    draw.rectangle((0, 618, 1200, 630), fill=(226, 171, 53))

    logo = Image.open(ROOT / "source" / "logo-full.png").convert("RGBA")
    logo.thumbnail((420, 420), Image.LANCZOS)
    og.paste(logo, (72, (630 - logo.height) // 2), logo)

    font_bold = str(ROOT / "source" / "fonts" / "BarlowCondensed-Bold.ttf")
    font_semi = str(ROOT / "source" / "fonts" / "BarlowCondensed-SemiBold.ttf")
    draw = ImageDraw.Draw(og)
    draw.rectangle((560, 152, 660, 158), fill=(226, 171, 53))
    draw.text((558, 184), "BUILD.", font=ImageFont.truetype(font_bold, 92), fill=(8, 13, 10))
    draw.text((558, 272), "CODE.", font=ImageFont.truetype(font_bold, 92), fill=(11, 58, 35))
    draw.text((558, 360), "COMPETE.", font=ImageFont.truetype(font_bold, 92), fill=(226, 171, 53))
    draw.text((560, 498), "COMBAT ROBOTICS  /  YUBA CITY, CA", font=ImageFont.truetype(font_semi, 24), fill=(93, 105, 99))
    draw.text((560, 536), "rvrobotics.ycusd.org", font=ImageFont.truetype(font_semi, 22), fill=(11, 58, 35))
    og.save(IMG / "og.jpg", "JPEG", quality=88, optimize=True)
    print("wrote assets/img/og.jpg")


if __name__ == "__main__":
    main()
