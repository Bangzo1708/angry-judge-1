#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one fixed, hand-written rant to /output/entry.txt.
Fully deterministic: the text is a constant, no randomness, no clock,
no external input. The rant is Variant A (self-checkout), chosen from
three candidates in variants.md as the strongest against the judge's
criteria: most rant-like anger, most original angle, strongest punch.
"""

import os

RANT = (
    "The self-checkout scanned my milk, then accused me of stealing it. "
    "'Unexpected item in the bagging area.' The item was the milk. "
    "I put it exactly where the machine told me to put it. "
    "A red light is flashing, an employee is strolling over at glacier speed, "
    "and I'm standing here like a criminal. Over $3.79 of dairy. "
    "I came in for milk. I'm leaving with a record."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()
