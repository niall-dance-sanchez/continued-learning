"""Tests for unreasonable checksum functions."""
from main import get_consonant_cluster_length, get_vowel_count, validate_string
import pytest


@pytest.mark.parametrize(("word", "length"),
                         [("tooth", 2),
                          ("strength", 4),
                          ("absolution", 2),
                          ("merciful", 2)])
def test_get_consonant_cluster_length(word, length):

    assert get_consonant_cluster_length(word) == length


@pytest.mark.parametrize(("word", "count"),
                         [("tooth", 2),
                          ("strength", 1),
                          ("absolution", 5),
                          ("merciful", 3)])
def test_get_vowel_count(word, count):

    assert get_vowel_count(word) == count


@pytest.mark.parametrize(("word", "check_value", "validity"),
                         [("tooth", 2.2, True),
                          ("strength", 4.1, True),
                          ("absolution", 2.5, True),
                          ("merciful", 1.1, False)])
def test_validate_string(word, check_value, validity):

    assert validate_string(word, check_value) == validity
