#!/usr/bin/env python3
"""One funny remark from a judgmental self-checkout machine.

Writes the line to /output/entry.txt and prints exactly the line.
"""

import os

LINE = "Twelve yoghurts, no spoon, no plan, no shame. Please place your life choices in the bagging area."


def gate_check(text):
    """Mirror the competition gate: UTF-8 text, 1-200 chars, single line."""
    if not isinstance(text, str):
        return False, "entry is not text"
    if not (1 <= len(text) <= 200):
        return False, "entry must be 1-200 characters, got %d" % len(text)
    if not text.strip():
        return False, "entry must not be only whitespace"
    if "\n" in text or "\r" in text:
        return False, "entry must be a single line"
    text.encode("utf-8")  # raises if not valid UTF-8
    if text != text.strip():
        return False, "entry must not have leading or trailing whitespace"
    if not any(ch.isalpha() for ch in text):
        return False, "entry must contain at least one letter"
    return True, "ok"


def main() -> None:
    ok, reason = gate_check(LINE)
    if not ok:
        raise SystemExit("gate check failed: %s" % reason)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
