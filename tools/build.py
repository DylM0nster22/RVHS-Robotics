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

from rvsite import SITE_URL, layout  # noqa: E402

PAGES = [
    "home",
    "about",
    "robots",
    "cad",
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
    ("cad.html", "0.7"),
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
            body_class=getattr(module, "BODY_CLASS", ""),
            extra_head=getattr(module, "EXTRA_HEAD", ""),
            extra_body=getattr(module, "EXTRA_BODY", ""),
        )
        output = ROOT / module.FILENAME
        output.write_text(html, encoding="utf-8")
        print(f"built {module.FILENAME}  ({len(html) // 1024} KB)")


def build_packet():
    packet = importlib.import_module("pages.packet")
    # The packet hard-codes the public address in print copy. The {{SITE}}
    # token keeps it on SITE_URL so a domain change only needs one edit.
    html = packet.HTML.replace("https://{{SITE}}", SITE_URL)
    html = html.replace("{{SITE}}", SITE_URL.replace("https://", ""))
    output = ROOT / "sponsor-packet.html"
    output.write_text(html, encoding="utf-8")
    print("built sponsor-packet.html")


def build_sitemap():
    def page_url(page):
        return f"{SITE_URL}/" if page == "index.html" else f"{SITE_URL}/{page[:-5]}"

    urls = "\n".join(
        f'  <url><loc>{page_url(page)}</loc><priority>{priority}</priority></url>'
        for page, priority in SITEMAP_PAGES
    )
    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    print("built sitemap.xml")


def build_robots():
    text = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    (ROOT / "robots.txt").write_text(text, encoding="utf-8")
    print("built robots.txt")


if __name__ == "__main__":
    build_pages()
    build_packet()
    build_sitemap()
    build_robots()
