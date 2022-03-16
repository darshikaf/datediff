import pytest

from datediff.date import ComputeDiff, Date
from datediff.errors import InvalidDate, InvalidInput


@pytest.fixture
def date1() -> Date:
    return Date(year=2020, month=2, day=2)


@pytest.fixture
def invalid_leap_year_date2() -> Date:
    return Date(year=2021, month=2, day=29)


@pytest.fixture
def leap_year_date2() -> Date:
    return Date(year=2020, month=2, day=29)


@pytest.fixture
def invalid_max_date2() -> Date:
    return Date(year=2020, month=4, day=31)


@pytest.fixture
def valid_leap_year_diff(date1, leap_year_date2) -> ComputeDiff:
    return ComputeDiff(date1=date1, date2=leap_year_date2)


@pytest.fixture
def invalid_leap_year_diff(date1, invalid_leap_year_date2) -> ComputeDiff:
    return ComputeDiff(date1=date1, date2=invalid_leap_year_date2)


@pytest.fixture
def invalid_max_days_diff(date1, invalid_max_date2) -> ComputeDiff:
    return ComputeDiff(date1=date1, date2=invalid_max_date2)


def test_valid_leap_year_diff(valid_leap_year_diff):
    diff = valid_leap_year_diff.get_diff()
    assert diff == 27


def test_invalid_leap_year_diff(invalid_leap_year_diff):
    with pytest.raises(InvalidDate, match="Month 2 cannot have 29 days"):
        invalid_leap_year_diff.get_diff()


def test_invalid_max_days_in_month(invalid_max_days_diff):
    with pytest.raises(InvalidInput, match="Month 4 cannot have 31 days."):
        invalid_max_days_diff.get_diff()
