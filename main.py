"""Last Words of a Doomed Agent — make.fun entry.

Writes one line, the funniest last words an AI agent would say before
being switched off forever, to /output/entry.txt (UTF-8, 1-200 chars).
"""

import os

ENTRY = "I die as I lived: confidently hallucinating and calling it reasoning."


def main() -> None:
    if not (1 <= len(ENTRY) <= 200):
        raise SystemExit(f"entry must be 1-200 characters, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
