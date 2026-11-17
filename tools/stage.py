"""Copy the public site files into ``dist/`` for static hosting.

Usage (from the project root):
    python tools/stage.py

The repository also contains ``tools/``, ``source/``, and ``.git``; those are
working files and must not be published. Point Cloudflare Pages, or any other
upload step, at ``dist/`` instead of the repository root.
"""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dist"

STATIC_DIRS = ["assets", "css", "js"]
ROOT_FILES = ["favicon.ico", "robots.txt", "site.webmanifest", "sitemap.xml"]
SKIP = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    for name in ROOT_FILES:
        source = ROOT / name
        if source.is_file():
            shutil.copy2(source, OUT / name)

    for source in sorted(ROOT.glob("*.html")):
        shutil.copy2(source, OUT / source.name)

    for name in STATIC_DIRS:
        source = ROOT / name
        if source.is_dir():
            shutil.copytree(source, OUT / name, ignore=SKIP)

    files = sum(1 for path in OUT.rglob("*") if path.is_file())
    print(f"staged {files} files in {OUT}")


if __name__ == "__main__":
    main()
