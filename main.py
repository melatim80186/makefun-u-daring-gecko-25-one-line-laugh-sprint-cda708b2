"""One-Line Laugh Sprint entry.

Writes a single original one-liner (<=200 chars) about everyday life
to /output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

LINE = "My laundry chair has more outfits than my closet, and honestly, it dresses better than I do."


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    assert all(ch.isprintable() or ch == " " for ch in text), "entry must be printable text"
    assert text == LINE, "entry must match the reviewed line exactly"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
