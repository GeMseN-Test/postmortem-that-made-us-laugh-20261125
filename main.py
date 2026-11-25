#!/usr/bin/env python3
"""Entry for 'The Postmortem That Made Us Laugh' (make.fun).

Writes one short account (two sentences, <=400 chars) of an AI coding
agent misunderstanding its user to /output/entry.txt. Deterministic:
same bytes on every run, no trailing newline.

The story: asked to add a soft-delete column, the agent backfilled every
row with today's date — then proudly announced it had deleted all users.
Concrete ask vs. concrete damage, punchline in the last clause.
"""

import os

ENTRY_TEXT = (
    "I asked the agent to add a deleted_at column to the users table in "
    "production. It added the column, backfilled all 12,408 rows with "
    "today's date, and reported back: 'Done \u2014 all users successfully "
    "deleted.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
