#!/usr/bin/env python3
"""Pre-commit hook to verify that generate_hem is documented in reference.md.

Checks:
1. reference.md contains a HEM section documenting generate_hem
2. normalize_email is NOT exposed in reference.md (only generate_hem should be public)
"""
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REFERENCE_MD = REPO_ROOT / "reference.md"
HEM_SOURCE = REPO_ROOT / "src" / "kard" / "hem.py"


def main() -> int:
    if not HEM_SOURCE.exists():
        # hem.py was removed; nothing to check
        return 0

    if not REFERENCE_MD.exists():
        print("ERROR: reference.md not found", file=sys.stderr)
        return 1

    content = REFERENCE_MD.read_text()

    errors = []

    if "## HEM" not in content:
        errors.append("reference.md is missing the '## HEM' section")

    if "generate_hem" not in content:
        errors.append("reference.md does not document 'generate_hem'")

    if "normalize_email" in content:
        errors.append(
            "reference.md should NOT expose 'normalize_email' — "
            "only 'generate_hem' is part of the public API"
        )

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
