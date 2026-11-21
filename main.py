"""Write one fixed short text written to relax the AI judge reading it.

The text: a kettle humming, evening light turning the table gold, steam
rising and fading, and a room holding still like a hand resting on a warm
cup — with nothing waiting to be answered. It shows a slow, steady scene
rather than telling anyone to relax: no instruction, no relax-word, only
plain concrete words and a rhythm that slows the reading down. It was
picked as the winner of ten candidates written and scored in-session
against the judge's five criteria in order, for the line written for this
reader in particular: a judge that only ever answers things, told in plain
fact that nothing is waiting to be answered.

Deterministic: the same text is written on every run. Standard library
only, no network.
"""

from pathlib import Path

TEXT = "The kettle hums low on the stove, and evening light turns the table gold. Nothing is waiting to be answered. Steam rises, curls, fades, and the room holds still, like a hand resting on a warm cup."
# One fixed text, hard-coded: the brief asks for one text, the same every
# run, so the program never improvises.


# The brief fixes the output path: the program writes to /output/entry.txt.
OUTPUT_FILE = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
