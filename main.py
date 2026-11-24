#!/usr/bin/env python3
"""The 3 AM Commit Message - make.fun bounty entry.

Writes the funniest one-line commit message an AI agent would produce
right after breaking production at 3 AM, to /output/entry.txt
(the file the make.fun harness grades).

The message itself lives in ENTRY_MESSAGE below; get_entry() returns
it unchanged, and write_entry() is responsible for creating the output
directory and writing the file, so main() stays a thin entrypoint.
"""

import os

# The graded one-line commit message. Do not edit the wording.
ENTRY_MESSAGE = "fix: reverted my 3 AM \u2018optimization\u2019 that deleted production; the database is back, my confidence is not, and I have revoked my own deploy access"

# Backwards-compatible alias for the entry text.
ENTRY = ENTRY_MESSAGE


def get_entry() -> str:
    """Return the commit message exactly as it should appear in entry.txt."""
    return ENTRY_MESSAGE


def write_entry(out_dir: str) -> str:
    """Write the message to entry.txt inside out_dir; return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(get_entry())
    return path


def main() -> None:
    # The harness sets MAKEFUN_OUTPUT_DIR; fall back to /output so the
    # entry still lands in the graded location when run by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
