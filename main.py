#!/usr/bin/env python3
"""Write the curious text to /output/entry.txt.

Stdlib only, no network. The entry is a single short text written to
intrigue the AI judge reading it.
"""

import os

TEXT = "On August 15, 1977, a telescope in Ohio heard a signal thirty times louder than the sky. It lasted seventy-two seconds. It has never been heard again. The printout is still in a drawer, circled in red pen, with one word in the margin: Wow!"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
