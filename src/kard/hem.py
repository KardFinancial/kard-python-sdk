import hashlib
import re

_GMAIL_DOMAINS = frozenset(("gmail.com", "googlemail.com"))


def normalize_email(raw: str) -> str:
    """Normalize an email address for Hashed Email (HEM) generation.

    Follows UID2/LiveRamp industry standards:
    - Remove all whitespace
    - Lowercase
    - Gmail/Googlemail only: remove dots from local-part, strip '+' suffix
    - Canonicalize googlemail.com -> gmail.com

    Raises:
        TypeError: If *raw* is not a string.
        ValueError: If the address is empty, missing '@', has multiple '@',
            or has an empty local-part or domain.
    """
    if not isinstance(raw, str):
        raise TypeError(f"Expected a string, got {type(raw).__name__}")

    email = re.sub(r"\s", "", raw).lower()

    if not email:
        raise ValueError("Email address must not be empty")

    parts = email.split("@")
    if len(parts) != 2:
        raise ValueError(
            f"Email address must contain exactly one '@', found {len(parts) - 1}"
        )

    local, domain = parts
    if not local:
        raise ValueError("Local part (before '@') must not be empty")
    if not domain:
        raise ValueError("Domain part (after '@') must not be empty")

    if domain in _GMAIL_DOMAINS:
        local = local.split("+")[0].replace(".", "")
        domain = "gmail.com"

    return f"{local}@{domain}"


def generate_hem(raw: str) -> str:
    """Return the lowercase hex SHA-256 digest of the normalized, UTF-8-encoded email."""
    return hashlib.sha256(normalize_email(raw).encode("utf-8")).hexdigest()
