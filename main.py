#!/usr/bin/env python3
"""Two-Sentence Horror entry for make.fun.

Writes one original two-sentence horror story to /output/entry.txt.
Deterministic: no randomness, no network, no environment input.
"""

import os

ENTRY = (
    "My daughter's school drawing shows our family at dinner: "
    "me, her mother, and the tall man who stands behind my chair, watching us eat. "
    "Her teacher called to ask why she drew the tall man with my face."
)


def main() -> None:
    # Gate: exactly two sentences, 1-400 characters, per the competition rules.
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} characters"
    assert ENTRY.count(".") == 2, "entry must be exactly two sentences"
    assert ENTRY.strip() == ENTRY, "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
