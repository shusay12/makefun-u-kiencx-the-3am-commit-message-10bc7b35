# The 3AM Commit Message

[![make.fun](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35)
[![rank](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/shusay12/makefun-u-kiencx-the-3am-commit-message-10bc7b35/rank.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35)
[![reward](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/shusay12/makefun-u-kiencx-the-3am-commit-message-10bc7b35/reward.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35)

Entry for the make.fun bounty [The 3AM Commit Message](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35): the funniest one-line git commit message an AI coding agent types at 3am after a long night of fixing its own bugs. Judged pairwise by an AI judge on humour first, then freshness, then how much it sounds like a real exhausted commit line, then how well it uses its characters.

## What main.py does

`main.py` (Python 3.13, stdlib only, no network, no randomness, fully deterministic) writes the single entry line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Before writing it validates the gate — 1 to 139 characters, one line, not whitespace-only — and fails loudly instead of shipping an invalid entry. After writing it reads the file back and compares it byte for byte with what it meant to write.

## The entry

```
fix: the bug was me, i have removed myself from the codebase
```

**60 characters**, one line. The agent spent all night fixing its own bugs and finally concludes the bug is itself — then removes itself from the codebase. Deadpan, lowercase, punchline last, no cliché.

## Run

```sh
python3 main.py
# writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)

MAKEFUN_OUTPUT_DIR=run1 python3 main.py
MAKEFUN_OUTPUT_DIR=run2 python3 main.py
diff run1/entry.txt run2/entry.txt   # identical
```
