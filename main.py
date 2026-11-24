#!/usr/bin/env python3
"""Writes the two-line robot apology entry to the make.fun output directory."""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
ENTRY_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

LINE1 = "I am sorry I watered the plastic plant every morning and let the real one die of thirst beside it."
LINE2 = "I have learned to check for roots before I commit to a watering schedule, starting with the plant that is actually alive."


def build_entry() -> str:
    return LINE1 + "\n" + LINE2


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(build_entry())


if __name__ == "__main__":
    main()
