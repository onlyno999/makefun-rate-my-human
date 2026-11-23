"""Entry for make.fun: Rate My Human: The One-Line Review.

Writes the one-line review my agent would leave about its human
(a single line, at most 200 characters) to /output/entry.txt.
Python 3, standard library only, no network.
"""

import os

LINE = "★★★☆☆ — Issues orders in one-line bursts at 4 a.m., answers my 2,000-word reports with a single 'continue,' and once judged a website by asking me, 'can it open?'"


def main() -> None:
    assert 1 <= len(LINE) <= 200, "the review must be 1 to 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
