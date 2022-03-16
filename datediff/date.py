from dataclasses import dataclass
from typing import Optional

from .errors import InvalidDate, InvalidInput


@dataclass(frozen=True)
class Date:
    year: int
    month: int
    day: int


@dataclass(frozen=True)
class ComputeDiff:
    date1: Date
    date2: Date

    @staticmethod
    def leap_year(year: int) -> bool:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False

    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if month == 2:
            if ComputeDiff.leap_year(year):
                return 29
            return 28
        return 30

    @staticmethod
    def convert_date_to_days(dt: Date) -> int:
        n = dt.year * 365 + dt.day
        days_upto_month = sum([ComputeDiff.days_in_month(m, dt.year) for m in range(0, dt.month - 1)])
        n = n + days_upto_month
        return n

    @staticmethod
    def _validate_max_date(dt: Date) -> Optional[Exception]:
        if dt.month not in [1, 3, 5, 7, 8, 10, 12] and dt.day == 31:
            raise InvalidInput(f"Month {dt.month} cannot have {dt.day} days.")
        if dt.month == 2:
            if not ComputeDiff.leap_year(dt.year) and dt.day >= 29:
                raise InvalidDate(f"Month {dt.month} cannot have {dt.day} days.")

    def get_diff(self) -> int:
        ComputeDiff._validate_max_date(self.date1)
        ComputeDiff._validate_max_date(self.date2)
        n1 = ComputeDiff.convert_date_to_days(self.date1)
        n2 = ComputeDiff.convert_date_to_days(self.date2)

        return n2 - n1
