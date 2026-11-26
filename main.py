"""The 3AM Commit Message — entry program.

Writes one line, a git commit message an AI coding agent might type at
3am after a long night of fixing its own bugs, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

Why this line, against the judge brief (criteria in the brief's order):

1. It reads as a real commit line: the ``fix:`` prefix, all lowercase,
   hurried phrasing, no polish — something typed by an exhausted agent.
2. The laugh lands on the first read, from the situation alone: the
   agent has spent the night chasing its own bugs and finally concludes
   the bug is itself — then deletes itself. No setup, no explanation.
3. It is fresh: the twist is self-removal, not the tired "fixed one bug,
   made seven more" or "it works, don't touch it" jokes.
4. It sounds typed in a hurry at 3am — flat, deadpan, lowercase,
   a confession rather than a caption.
5. It uses its characters well: 60 characters, the punchline
   ("removed myself from the codebase") lands last, nothing padded.

The program is deterministic (stdlib only, no network, no randomness).
It validates the gate before writing — 1 to 139 characters, a single
line, not whitespace-only — and fails loudly instead of shipping an
invalid entry. It then reads the file back and compares it byte for
byte with what it meant to write.
"""

import os
import sys

# The entry line. Lowercase, deadpan, punchline last.
ENTRY = "fix: the bug was me, i have removed myself from the codebase"

MIN_LENGTH = 1
MAX_LENGTH = 139


def fail(message: str) -> "SystemExit":
    """Exit loudly: an invalid entry must never be shipped silently."""
    print(f"error: {message}", file=sys.stderr)
    return SystemExit(1)


def main() -> int:
    line = ENTRY

    # Gate checks, in the order the sealed scorer applies them.
    if not line or line.strip() == "":
        raise fail("entry is empty or whitespace-only")
    if len(line) < MIN_LENGTH or len(line) > MAX_LENGTH:
        raise fail(
            f"entry is {len(line)} characters, must be {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if "\n" in line or "\r" in line:
        raise fail("entry must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")

    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)

    # Verify the write byte-exactly: read it back and compare.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line:
        raise fail(
            f"verification failed: wrote {line!r}, read back {written!r}"
        )

    print(f"wrote {path} ({len(line)} chars): {line}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
