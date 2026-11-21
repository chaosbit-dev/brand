"""Render the App avatar SVGs to PNG, plus a contact sheet for checking small sizes.

Usage: python3 scripts/render.py [name ...]   (default: every apps/*.svg)

Output goes to out/, which is gitignored: PNGs are build products, regenerate them.
Needs Google Chrome; set CHROME to its binary if it isn't in the macOS default spot.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPS = ROOT / "apps"
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
    small = "".join(
        f'<img src="{p.name}" width="40" style="border-radius:50%">' for p in pngs
    ) + "".join(f'<img src="{p.name}" width="20">' for p in pngs)
    html = OUT / "sheet.html"
    html.write_text(
        '<html><body style="margin:0;background:#fff;padding:16px;width:900px">'
        f'<div style="display:flex;flex-wrap:wrap;gap:12px">{big}</div>'
        f'<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center;'
        f'margin-top:12px">{small}</div></body></html>'
    )
    rows = -(-len(pngs) // 4)
    sheet = OUT / "sheet.png"
    screenshot(html, sheet, 900, rows * 236 + 120)
    return sheet


def main(names: list[str]) -> None:
    sources = (
        [APPS / f"{n}.svg" for n in names]
        if names
        else sorted(p for p in APPS.glob("*.svg") if not p.name.startswith("_"))
    )
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
