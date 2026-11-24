"""Write the tournament-winning loading-screen tip to /output/entry.txt.

Tournament winner H (93 bytes): the agent named the variable final_final_v2.
It knows. It is sorry. It will do it again.
"""

import os

# Competition gate: the entry must fit the 200-character limit.
MAX_CHARS = 200

ENTRY = "Tip: the agent named the variable final_final_v2. It knows. It is sorry. It will do it again."

# Enforce the competition gate on the final text itself.
assert len(ENTRY) <= MAX_CHARS, f"entry must be <= {MAX_CHARS} chars, got {len(ENTRY)}"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Self-check: read back and verify the written file matches exactly.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "entry.txt does not match the winning line"
    assert len(data) == 93, f"entry.txt must be 93 bytes, got {len(data)}"
    assert b"final_final_v2" in data, "entry.txt must contain the payoff variable name"
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"


if __name__ == "__main__":
    main()
