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
    """
    email = re.sub(r"\s", "", raw).lower()
    local, domain = email.rsplit("@", 1)

    if domain in _GMAIL_DOMAINS:
        local = local.split("+")[0].replace(".", "")
        domain = "gmail.com"

    return f"{local}@{domain}"


def generate_hem(raw: str) -> str:
    """Return the lowercase hex SHA-256 digest of the normalized, UTF-8-encoded email."""
    return hashlib.sha256(normalize_email(raw).encode("utf-8")).hexdigest()
