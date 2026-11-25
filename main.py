"""One Word From Grandma — v2 entry.

Grandma cannot remember what the thing is called, so she calls it what she
calls every gadget she cannot name. That one word is the whole joke: warm,
baffled, and unmistakably hers. This program writes that word, and nothing
else, to /output/entry.txt.
"""

from pathlib import Path

# The word Grandma would text about AI: the name she gives any clever
# machine she cannot name, typed exactly as she would type it.
WORD = "thingamajig"

OUT_PATH = Path("/output/entry.txt")


def pick_word() -> str:
    """Return the entry word, cleaned and checked against the gate."""
    word = WORD.strip()
    if not word or len(word) > 30 or len(word.split()) != 1:
        raise ValueError("entry must be a single word of 1-30 characters")
    return word


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(pick_word(), encoding="utf-8")


if __name__ == "__main__":
    main()
