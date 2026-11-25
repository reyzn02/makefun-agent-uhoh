#!/usr/bin/env python3
"""The Agent's Uh-Oh -- make.fun entry.

Writes the one word an agent says when it has no idea what to do
to /output/entry.txt.

The word is "recalculating": the honest blurt of a machine that has
lost its way. A sat-nav says it when you miss the turn; an agent
says it when the plan falls apart and it has to start over. It is a
genuine one-word reaction to being completely lost, it sounds like
something a machine would actually say mid-task, and it lands the
moment you read it -- no caption needed.

Stdlib only, no network access, deterministic: the same word every run.
"""

import os

WORD = "recalculating"


def validate(word):
    """Check the word against the competition gate before writing it."""
    if not isinstance(word, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(word) <= 99:
        raise ValueError("entry must be 1 to 99 characters")
    if not word.strip():
        raise ValueError("entry must not be only white space")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    word.encode("utf-8")  # must be valid UTF-8 text
    return word


def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    word = validate(WORD)
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    print("wrote %d characters to %s: %s" % (len(word), path, word))


if __name__ == "__main__":
    main()
