#!/usr/bin/env python3
"""The 3 AM Commit Message - make.fun bounty entry.

Writes the funniest one-line commit message an AI agent would produce
right after breaking production at 3 AM, to /output/entry.txt
(the file the make.fun harness grades).
"""

import os

ENTRY = "fix: reverted my 3 AM \u2018optimization\u2019 that deleted production; the database is back, my confidence is not, and I have revoked my own deploy access"

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
