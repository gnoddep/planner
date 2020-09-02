import calendar
import datetime
from typing import List, Set, Tuple

from .planning import Planning

_LAST_DAY_OF_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class DayOfMonth(Planning):
    def __init__(self, day: int, *days: int):
        self.__days = {day, *days}
        for day in self.__days:
            assert 1 <= abs(day) <= 31

    @property
    def days(self) -> Set[int]:
        return self.__days

    def match(self, date: datetime.datetime) -> bool:
        return date.day in self.__get_days_of_month(date.year, date.month)

    def next(self, date: datetime.datetime) -> datetime.datetime:
        year = date.year
        month = date.month
        day = date.day

        while True:
            days_of_month = self.__get_days_of_month(year, month)
            while not days_of_month or day >= days_of_month[-1]:
                year, month, day = self.__next_month(year, month)
                days_of_month = self.__get_days_of_month(year, month)

            for dom in days_of_month:
                if day < dom:
                    return datetime.datetime(year=year, month=month, day=dom, tzinfo=date.tzinfo)

            year, month, day = self.__next_month(year, month)

    @staticmethod
    def __next_month(year: int, month: int) -> Tuple[int, int, int]:
        if month == 12:
            return year + 1, 1, 0
        return year, month + 1, 0

    def __get_days_of_month(self, year: int, month: int) -> List[int]:
        days_of_month = set()
        for dom in self.__days:
            last_day_of_month = _LAST_DAY_OF_MONTH[month] + int(month == 2 and calendar.isleap(year))

            if dom < 0:
                dom = last_day_of_month + dom + 1

            if 0 < dom <= last_day_of_month:
                days_of_month.add(dom)

        return sorted(days_of_month)
