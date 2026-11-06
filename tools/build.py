"""Build the River Valley Robotics static site.

Usage (from the project root):
    python tools/build.py
"""
import importlib
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

from rvsite import layout  # noqa: E402

PAGES = [
    "home",
    "about",
    "robots",
    "sponsors",
    "gallery",
    "watch",
    "join",
    "contact",
    "credits",
    "accessibility",
    "notfound",
]

SITEMAP_PAGES = [
    ("index.html", "1.0"),
    ("about.html", "0.8"),
    ("robots.html", "0.8"),
    ("sponsors.html", "0.9"),
    ("gallery.html", "0.6"),
    ("watch.html", "0.7"),
    ("join.html", "0.8"),
    ("contact.html", "0.7"),
    ("credits.html", "0.2"),
    ("accessibility.html", "0.2"),
]


def build_pages():
    for name in PAGES:
        module = importlib.import_module(f"pages.{name}")
        html = layout(
            module.TITLE,
            module.DESCRIPTION,
            getattr(module, "ACTIVE", ""),
            module.BODY,
            filename=module.FILENAME,
            robots=getattr(module, "ROBOTS", "index, follow"),
        )
        output = ROOT / module.FILENAME
        output.write_text(html, encoding="utf-8")
        print(f"built {module.FILENAME}  ({len(html) // 1024} KB)")


def build_packet():
    packet = importlib.import_module("pages.packet")
    output = ROOT / "sponsor-packet.html"
    output.write_text(packet.HTML, encoding="utf-8")
    print("built sponsor-packet.html")


def build_sitemap():
    urls = "\n".join(
        f'  <url><loc>https://rvrobotics.ycusd.org/{"" if page == "index.html" else page}</loc><priority>{priority}</priority></url>'
        for page, priority in SITEMAP_PAGES
    )
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print("built sitemap.xml")


if __name__ == "__main__":
    build_pages()
    build_packet()
    build_sitemap()
