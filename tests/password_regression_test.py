"""Regression tests for password validation (expected behavior matches the repo's initial commit)."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import UserProfile


@pytest.mark.parametrize(
    "password",
    [
        "aA1!abcdef",  # uppercase not at start; meets length and character-class rules
        "aA1!abcd",  # minimum length 8
        "x9Z!zzzzzz",  # digit before letters; mixed case and special
    ],
)
def test_valid_password_rules_accepted_when_requirements_met_anywhere(password: str):
    """Passwords that include upper, lower, digit, special, and length ≥8 must be accepted."""
    assert UserProfile.valid_password(password) is True
