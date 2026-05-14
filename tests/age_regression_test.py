import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src import Location, UserProfile


def _profile(dob: str) -> UserProfile:
    loc = Location(city="Springfield", state="IL", country="US")
    return UserProfile(
        name="John Smith",
        email="john@example.com",
        password="Aa1!aaaa",
        dob=dob,
        location=loc,
    )


def test_age_on_birthday_matches_calendar_year_difference():
    """Age on one's birthday must equal (reference year − birth year), not one less."""
    user = _profile("2000-05-14")
    reference = datetime(2026, 5, 14)
    assert user.get_age(reference) == 26


def test_age_later_same_month_after_birthday():
    """After the birthday in the same month, age must not be reduced by an extra year."""
    user = _profile("2000-05-14")
    reference = datetime(2026, 5, 20)
    assert user.get_age(reference) == 26


def test_age_mm_dd_yyyy_format_consistent():
    user = _profile("05/14/2000")
    reference = datetime(2026, 5, 14)
    assert user.get_age(reference) == 26
