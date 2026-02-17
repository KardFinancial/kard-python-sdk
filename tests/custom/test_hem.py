import json
import os

import pytest

from kard.hem import generate_hem, normalize_email

_VECTORS_PATH = os.path.join(os.path.dirname(__file__), "test_vectors.json")

with open(_VECTORS_PATH, encoding="utf-8") as f:
    vectors = json.load(f)


@pytest.mark.parametrize("vector", vectors, ids=[v["name"] for v in vectors])
def test_normalize_email(vector: dict) -> None:
    assert normalize_email(vector["input"]) == vector["normalized"]


@pytest.mark.parametrize("vector", vectors, ids=[v["name"] for v in vectors])
def test_generate_hem(vector: dict) -> None:
    assert generate_hem(vector["input"]) == vector["sha256_hex"]


@pytest.mark.parametrize(
    "raw, error_type, match",
    [
        ("", ValueError, "must not be empty"),
        ("   ", ValueError, "must not be empty"),
        ("\t\n", ValueError, "must not be empty"),
        ("noatsign", ValueError, "exactly one '@'"),
        ("a@b@c", ValueError, "exactly one '@'"),
        ("@domain.com", ValueError, "Local part"),
        ("user@", ValueError, "Domain part"),
        ("@", ValueError, "Local part"),
        (None, TypeError, "Expected a string"),
        (123, TypeError, "Expected a string"),
    ],
    ids=[
        "empty string",
        "only spaces",
        "only whitespace",
        "no @",
        "multiple @",
        "empty local",
        "empty domain",
        "bare @",
        "None input",
        "int input",
    ],
)
def test_normalize_email_rejects_invalid(raw, error_type, match) -> None:
    with pytest.raises(error_type, match=match):
        normalize_email(raw)
