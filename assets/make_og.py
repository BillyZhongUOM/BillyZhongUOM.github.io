#!/usr/bin/env python3
"""Generate the Open Graph social card (1200x630) for the personal site.

Matches the site's light theme: warm paper background, Oxford-navy ink and
accent bar. Run from anywhere: python3 assets/make_og.py
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent / "og.png"

W, H = 1200, 630
BG = (250, 249, 246)       # --bg
INK = (22, 32, 42)         # --ink
MUTED = (88, 100, 113)     # --muted
ACCENT = (11, 61, 107)     # --accent (Oxford navy)

# System font candidates (macOS first, then common fallbacks).
SERIF_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "/Library/Fonts/Georgia.ttf",
    "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
]
SANS_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/Library/Fonts/Arial.ttf",
]
SANS_BOLD_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/Library/Fonts/Arial Bold.ttf",
]


def load(cands, size):
    for p in cands:
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return ImageFont.load_default()


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    serif_xl = load(SERIF_CANDIDATES, 92)
    sans_md = load(SANS_BOLD_CANDIDATES or SANS_CANDIDATES, 36)
    sans_sm = load(SANS_CANDIDATES, 30)

    pad = 88

    # Accent bar at the top-left.
    d.rectangle([pad, pad, pad + 88, pad + 12], fill=ACCENT)

    # Eyebrow.
    d.text((pad, pad + 34), "UNIVERSITY OF OXFORD", font=sans_sm, fill=ACCENT)

    # Name.
    d.text((pad - 2, pad + 96), "Xiaomin Zhong", font=serif_xl, fill=INK)

    # Role.
    d.text((pad, pad + 220), "Health Data Epidemiologist", font=sans_md, fill=INK)

    # One-line positioning.
    d.text(
        (pad, pad + 300),
        "National electronic health records, for safer hospital care.",
        font=sans_sm,
        fill=MUTED,
    )

    # Monogram chip bottom-right.
    chip = 132
    cx0 = W - pad - chip
    cy0 = H - pad - chip
    d.rounded_rectangle([cx0, cy0, cx0 + chip, cy0 + chip], radius=22, fill=ACCENT)
    mono = load(SERIF_CANDIDATES, 64)
    tb = d.textbbox((0, 0), "XZ", font=mono)
    tw, th = tb[2] - tb[0], tb[3] - tb[1]
    d.text((cx0 + (chip - tw) / 2 - tb[0], cy0 + (chip - th) / 2 - tb[1]), "XZ",
           font=mono, fill=(255, 255, 255))

    # Footer profile line.
    d.text((pad, H - pad - 14), "scholar.google.com  ·  ndph.ox.ac.uk", font=sans_sm, fill=MUTED)

    img.save(OUT, "PNG")
    print(f"Wrote {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()
