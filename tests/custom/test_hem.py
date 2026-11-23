import pytest

from kard.hem import normalize_email


@pytest.mark.parametrize("raw", ["+tag@gmail.com", "...@googlemail.com"])
def test_gmail_local_part_empty_after_normalization(raw: str) -> None:
    with pytest.raises(ValueError, match="Local part"):
        normalize_email(raw)
