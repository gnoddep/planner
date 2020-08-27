import calendar
import datetime
from typing import Tuple

from .planning import Planning

LAST_DAY_OF_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class DayOfMonth(Planning):
    def __init__(self, day: int):
        assert 1 <= abs(day) <= 31
        self.__day = day

    @property
    def day(self) -> int:
        return self.__day

    def match(self, date: datetime.datetime) -> bool:
        return date.day == self.__get_day_of_month(date.year, date.month)

    def next(self, date: datetime.datetime) -> datetime.datetime:
        year = date.year
        month = date.month
        day = date.day

        while not day < self.__get_day_of_month(year, month) <= self.__get_last_day_of_month(year, month):
            day = 0
            year, month = self.__next_month(year, month)

        return datetime.datetime(year=year, month=month, day=self.__get_day_of_month(year, month), tzinfo=date.tzinfo)

    def __get_day_of_month(self, year: int, month: int) -> int:
        if self.__day < 0:
            return self.__get_last_day_of_month(year, month) + self.__day + 1
        return self.__day

    @staticmethod
    def __get_last_day_of_month(year: int, month: int) -> int:
        return LAST_DAY_OF_MONTH[month] + int(month == 2 and calendar.isleap(year))

    @staticmethod
    def __next_month(year: int, month: int) -> Tuple[int, int]:
        if month == 12:
            return year + 1, 1
        return year, month + 1
