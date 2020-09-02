import datetime
from typing import List

from .planning import Planning


class Month(Planning):
    def __init__(self, month: int, *months: int):
        self.__months = sorted({month, *months})
        for month in self.__months:
            assert 1 <= month <= 12

    @property
    def months(self) -> List[int]:
        return self.__months

    def match(self, date: datetime.datetime) -> bool:
        return date.month in self.__months

    def next(self, date: datetime.datetime) -> datetime.datetime:
        if date.month >= self.__months[-1]:
            return datetime.datetime(year=date.year + 1, month=self.__months[0], day=1, tzinfo=date.tzinfo)

        for month in self.__months:
            if date.month < month:
                return datetime.datetime(year=date.year, month=month, day=1, tzinfo=date.tzinfo)
