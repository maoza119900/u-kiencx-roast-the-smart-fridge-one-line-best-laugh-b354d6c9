"""Roast the Smart Fridge: One Line, Best Laugh Wins — make.fun entry.

Writes a single original roast line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(default ``/output/entry.txt``) and prints it to stdout.

The line is a fixed string constant: the program reads no clock, no
randomness, no network and no files, so every run produces byte-identical
output. At 114 characters it sits inside the gate's 1–160 character limit.
"""

import os
import sys

ENTRY = (
    "My smart fridge texts me that the milk expires tomorrow, like a "
    "snitch in my own kitchen ratting out my leftovers."
)


def main() -> int:
    # Self-check the sealed gate before writing: UTF-8 text, 1–160
    # characters, not only whitespace. A line outside it scores Valid 0
    # and is never judged, so fail loudly here instead of shipping it.
    if not 1 <= len(ENTRY) <= 160 or not ENTRY.strip():
        raise SystemExit(
            f"entry line is {len(ENTRY)} characters; gate needs 1-160"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
