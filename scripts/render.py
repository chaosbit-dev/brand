"""Render the avatar SVGs (apps/ and accounts/) to PNG, plus a contact sheet for checking small sizes.

Usage: python3 scripts/render.py [name ...]   (default: every apps/*.svg and accounts/*.svg)

Output goes to out/, which is gitignored: PNGs are build products, regenerate them.
Needs Google Chrome; set CHROME to its binary if it isn't in the macOS default spot.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = (ROOT / "apps", ROOT / "accounts")
OUT = ROOT / "out"
CHROME = os.environ.get(
    "CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)
SIZE = 512


def screenshot(src: Path, dest: Path, width: int, height: int) -> None:
    subprocess.run(
        [
            CHROME,
            "--headless",
            "--disable-gpu",
            "--hide-scrollbars",
            f"--window-size={width},{height}",
            f"--screenshot={dest}",
            src.as_uri(),
        ],
        check=True,
        capture_output=True,
    )


def contact_sheet(pngs: list[Path]) -> Path:
    big = "".join(
        f'<div style="text-align:center;font:12px sans-serif">'
        f'<img src="{p.name}" width="200"><br>{p.stem}</div>'
        for p in pngs
    )
    row = '<div style="display:flex;gap:8px;align-items:center;margin-top:12px">'
    small = (
        row
        + "".join(
            f'<img src="{p.name}" width="40" style="border-radius:50%">' for p in pngs
        )
        + "</div>"
        + row
        + "".join(f'<img src="{p.name}" width="20">' for p in pngs)
        + "</div>"
    )
    html = OUT / "sheet.html"
    html.write_text(
        '<html><body style="margin:0;background:#fff;padding:16px;width:900px">'
        f'<div style="display:flex;flex-wrap:wrap;gap:12px">{big}</div>'
        f"{small}</body></html>"
    )
    rows = -(-len(pngs) // 4)
    sheet = OUT / "sheet.png"
    screenshot(html, sheet, 900, rows * 236 + 140)
    return sheet


def main(names: list[str]) -> None:
    every = sorted(
        (p for d in SOURCES for p in d.glob("*.svg") if not p.name.startswith("_")),
        key=lambda p: p.stem,
    )
    by_name = {p.stem: p for p in every}
    sources = [by_name[n] for n in names] if names else every
    OUT.mkdir(exist_ok=True)
    pngs = []
    for src in sources:
        dest = OUT / f"{src.stem}.png"
        screenshot(src, dest, SIZE, SIZE)
        pngs.append(dest)
        print(dest.relative_to(ROOT))
    print(contact_sheet(pngs).relative_to(ROOT))


if __name__ == "__main__":
    main(sys.argv[1:])
