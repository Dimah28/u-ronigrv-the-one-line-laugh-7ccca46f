#!/usr/bin/env python3
"""The One-Line Laugh (make.fun bounty u-ronigrv-the-one-line-laugh-7ccca46f).

Writes one original funny line to /output/entry.txt.

The line was built for this bounty judge's own criteria, in order:
  1. Funny, within 200 characters: a single sentence of 98 characters.
  2. A real surprise at the end that still makes sense: the twist is
     that the gym building itself "believes in" the narrator -- the
     membership is reframed as buying faith, not fitness, and the
     punch lands on the last words ("more than I do").
  3. An everyday truth people recognise: paying every month for a gym
     membership you barely use.
  4. Economical: one sentence, every word earns its place, nothing
     there to explain the joke.
  5. Fresh: the "building believes in me" turn is not a stock gym
     punchline; it is a self-own with a new image.

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

JOKE = "I pay for a gym membership every month so a building across town can believe in me more than I do."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(joke: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, a single sentence, at least one character that is not white
    space. Fail loudly instead of writing an entry the gate would refuse."""
    if not 1 <= len(joke) <= 200:
        raise SystemExit(f"joke is {len(joke)} characters, must be 1-200")
    if joke.count(".") != 1 or not joke.endswith("."):
        raise SystemExit("joke must be a single sentence")
    if not any(not ch.isspace() for ch in joke):
        raise SystemExit("joke must contain a non-whitespace character")


def main() -> None:
    validate(JOKE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the joke: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
