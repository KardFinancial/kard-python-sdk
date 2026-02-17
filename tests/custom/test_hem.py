import json
import os

import pytest

from kard.hem import generate_hem, normalize_email

_VECTORS_PATH = os.path.join(os.path.dirname(__file__), "test_vectors.json")

with open(_VECTORS_PATH) as f:
    vectors = json.load(f)


@pytest.mark.parametrize("vector", vectors, ids=[v["name"] for v in vectors])
def test_normalize_email(vector: dict) -> None:
    assert normalize_email(vector["input"]) == vector["normalized"]


@pytest.mark.parametrize("vector", vectors, ids=[v["name"] for v in vectors])
def test_generate_hem(vector: dict) -> None:
    assert generate_hem(vector["input"]) == vector["sha256_hex"]
