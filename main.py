#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Tell a Whole Story in 32 Characters" - in the kit
this is a Wi-Fi network name of at most 32 characters that lands a joke
and implies a whole story.
Candidates compared: 'MomClickedThePopUpAgain' (a character and a repeat
accident, but the damage stays vague), 'ExStillPaysForThisWiFi' (clear
story, yet the joke is just smugness), and the selected
'DadFellForThePrinceEmail': a character, a famous scam and a whole
family disaster in 24 characters, readable aloud in a network list,
with every character earning its place under the 32-character gate.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "DadFellForThePrinceEmail"
TEXT = LINE + "\n"
MAX_CHARS = 32


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
