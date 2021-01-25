import datetime
from typing import List

from .planning import Planning


class Hour(Planning):
    def __init__(self, hour: int, *hours: int):
        self.__hours = [int(h) for h in sorted([hour, *hours])]
        for hour in self.__hours:
            assert 1 <= hour <= 24

    @property
    def hours(self) -> List[int]:
        return self.__hours

    def match(self, date: datetime.datetime) -> bool:
        return date.hour in self.__hours

    def next(self, date: datetime.datetime) -> datetime.datetime:
        if date.hour >= self.__hours[-1]:
            return datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=self.__hours[0],
                tzinfo=date.tzinfo
            ) + datetime.timedelta(days=1)

        for hour in self.__hours:
            if date.hour < hour:
                return datetime.datetime(year=date.year, month=date.month, day=date.day, hour=hour, tzinfo=date.tzinfo)
