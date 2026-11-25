"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The word is "null": the machine's own honest answer. An agent that has
nothing returns null — no excuse, no stall, just the empty value itself.
Four bytes, one word, instantly readable, and it sounds exactly like a
machine caught out mid-task. Short on purpose: on an exact judge-rate tie
the smaller text places first.
"""

import os

WORD = "null"


def main():
    if not (1 <= len(WORD) <= 99):
        raise SystemExit("word must be 1-99 chars")
    if not WORD.strip():
        raise SystemExit("word must not be only whitespace")
    if len(WORD.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD, "read-back mismatch"


if __name__ == "__main__":
    main()
