import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_zeros_and_negatives():
    assert longest_positive_streak([-1, -2, 0, -3]) == 0
    assert longest_positive_streak([1, 2, 0, 3, 4, 5, -1, 6]) == 3

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_element_list():
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([-1]) == 0
    assert longest_positive_streak([0]) == 0

def test_streak_at_the_end():
    # The original implementation had a bug where it would not correctly
    # account for a streak that ended at the last element. This test
    # specifically covers that case.
    assert longest_positive_streak([1, 2, 0, 3, 4]) == 2
    assert longest_positive_streak([-1, 0, 1, 2, 3, 4, 5]) == 5
