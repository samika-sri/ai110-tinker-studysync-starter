"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

from scoring import session_rating


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


# TODO: add at least one more test, e.g. a boundary case for "Skip" (a score
# of 59) or the exact boundary for "Good" (a score of 80).

def test_session_rating_boundary_59_is_skip():
    assert session_rating(59) == "Skip"


# Part 3: the reachable range is 0-100 (0-60 sliders, capped by apply_streak_bonus),


def test_session_rating_boundary_60_is_meh():
    assert session_rating(60) == "Meh"


def test_session_rating_boundary_70_is_ok():
    assert session_rating(69) == "Meh"
    assert session_rating(70) == "OK"


def test_session_rating_boundary_80_is_good():
    assert session_rating(79) == "OK"
    assert session_rating(80) == "Good"


def test_session_rating_boundary_89_is_good():
    assert session_rating(89) == "Good"


def test_session_rating_top_of_range_is_great():
    assert session_rating(100) == "Great"
