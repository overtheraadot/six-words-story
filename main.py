#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry (account A / overtheraa).

Writes exactly one six-word story to <MAKEFUN_OUTPUT_DIR>/entry.txt.
Deterministic, no network, no model calls, no file reads outside the repo.
"""

import os

STORY = "Sold her piano, kept the lullaby."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
