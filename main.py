"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word a grandma
would text her grandchild about AI.
"""

from pathlib import Path

# Grandma heard the grandkids talking about ChatGPT. She typed it from
# memory, the way she heard it, and autocorrect did the rest.
GRANDMAS_WORD = "catgpt"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # One word, no spaces, no punctuation tricks — just grandma's text.
    word = GRANDMAS_WORD.strip()
    assert " " not in word and word.isalpha()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
