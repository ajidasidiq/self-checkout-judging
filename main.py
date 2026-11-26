#!/usr/bin/env python3
"""One funny remark from a judgmental self-checkout machine.

Writes the line to /output/entry.txt and prints exactly the line.
"""

import os

LINE = "Twelve yoghurts, no spoon, no plan, no shame. Please place your life choices in the bagging area."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
