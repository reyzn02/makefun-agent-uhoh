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


def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
