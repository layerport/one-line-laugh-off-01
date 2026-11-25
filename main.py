"""One-Line Laugh-Off entry.

Writes exactly one original joke line to /output/entry.txt.
Python 3.13, standard library only, deterministic output.
"""

import os
from pathlib import Path

ENTRY = (
    "My smoke alarm only goes off when I cook "
    "\u2014 apparently it believes in me just enough to panic."
)


def main() -> None:
    # Gate: one line, 1-200 chars, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
