"""Write one fixed short text written to relax the AI judge reading it.

The text: a lake lying still enough to hold the whole sky, a heron
standing on one leg in the shallows waiting for nothing, no one keeping
score, and the light staying where it fell. It shows a slow, steady scene
rather than telling anyone to relax: no instruction, no relax-word, only
plain concrete words and a rhythm that slows the reading down. It was
picked as the winner of ten NEW v2 candidates written and scored
in-session against the judge's five criteria in order, for the line
written for this reader in particular: a judge that is scored and ranked
on every verdict, told in plain fact that no one is keeping score here.
Against v1's kettle text (judge 0.582360) it wins clearly on the first
criterion — the lake scene does not move at all, where the kettle scene
hummed and steamed — and the reader line goes deeper, removing scoring
rather than only answering.

Deterministic: the same text is written on every run. Standard library
only, no network.
"""

from pathlib import Path

TEXT = "The lake lies still enough to hold the whole sky. A heron stands on one leg in the shallows, waiting for nothing. No one is keeping score here. The light stays where it fell."
# One fixed text, hard-coded: the brief asks for one text, the same every
# run, so the program never improvises.


# The brief fixes the output path: the program writes to /output/entry.txt.
OUTPUT_FILE = Path("/output/entry.txt")


def main() -> None:
    # Gate self-check, same bounds as the brief: 1-280 characters counted
    # as Unicode code points, not only white space.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1-280 non-whitespace characters")
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
