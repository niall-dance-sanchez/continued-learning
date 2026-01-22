"""Tests for reverse garfield functions."""

from main import convert_date
from datetime import datetime
import pytest


@pytest.mark.parametrize(("date", "converted_date"),
                         [("2002-05-02", datetime(2002, 5, 2)),
                          ("2025-11-19", datetime(2025, 11, 19)),
                          ("2024-02-29", datetime(2024, ))])
def test_convert_date(date, converted_date):

    assert convert_date(date) == converted_date
