"""Prepare the team's official logo for the web (remove white background, resize)."""
from collections import deque
from pathlib import Path

from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "assets" / "img"
SRC = ROOT / "source" / "logo.jpg"

image = Image.open(SRC).convert("RGBA")
pixels = image.load()
width, height = image.size

# Flood-fill near-white background from every edge, leaving enclosed white
# lettering and highlights untouched.
visited = bytearray(width * height)
queue = deque()


def is_background(x, y):
    r, g, b, _ = pixels[x, y]
    return r > 236 and g > 236 and b > 236 and max(r, g, b) - min(r, g, b) < 10


for x in range(width):
    for y in (0, height - 1):
        if is_background(x, y):
            queue.append((x, y))
            visited[y * width + x] = 1
for y in range(height):
    for x in (0, width - 1):
        if is_background(x, y) and not visited[y * width + x]:
            queue.append((x, y))
            visited[y * width + x] = 1

while queue:
    x, y = queue.popleft()
    pixels[x, y] = (pixels[x, y][0], pixels[x, y][1], pixels[x, y][2], 0)
    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if 0 <= nx < width and 0 <= ny < height and not visited[ny * width + nx]:
            if is_background(nx, ny):
                visited[ny * width + nx] = 1
                queue.append((nx, ny))

# Slightly feather the cut edge so it does not look jagged on dark backgrounds.
alpha = image.getchannel("A").filter(ImageFilter.GaussianBlur(0.6))
image.putalpha(alpha)

bbox = image.getbbox()
image = image.crop((max(0, bbox[0] - 6), max(0, bbox[1] - 6), min(width, bbox[2] + 6), min(height, bbox[3] + 6)))
print("logo size", image.size)

logo_full = ROOT / "source" / "logo-full.png"
logo_full.parent.mkdir(parents=True, exist_ok=True)
image.save(logo_full, "PNG", optimize=True)

footer = image.resize((360, round(360 * image.height / image.width)), Image.LANCZOS)
footer.save(IMG / "logo-footer.webp", "WEBP", quality=90, method=6)
print("wrote logo-footer.webp")

# Just the falcon head for the compact header mark and app icon.
mark = image.crop((190, 15, 970, 610))
mark.resize((300, round(300 * mark.height / mark.width)), Image.LANCZOS).save(
    IMG / "logo-mark.webp", "WEBP", quality=90, method=6
)
print("mark size", mark.size)

# App icon: the falcon mark on a warm paper square.
from PIL import ImageDraw

size = 512
icon = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(icon)
draw.rounded_rectangle((0, 0, size, size), radius=104, fill=(246, 243, 234, 255))
head = mark.copy()
head.thumbnail((size - 50, size - 50), Image.LANCZOS)
icon.alpha_composite(head, ((size - head.width) // 2, (size - head.height) // 2))
icon.save(IMG / "icon-512.png", "PNG")
icon.resize((192, 192), Image.LANCZOS).save(IMG / "icon-192.png", "PNG")
icon.resize((32, 32), Image.LANCZOS).save(IMG / "favicon-32.png", "PNG")
print("wrote icons")
