import datetime
from typing import List

from .planning import Planning


class Minute(Planning):
    def __init__(self, minute: int, *minutes: int):
        self.__minutes = [int(m) for m in sorted([minute, *minutes])]
        for minute in self.__minutes:
            assert 0 <= minute < 60

    @property
    def minutes(self) -> List[int]:
        return self.__minutes

    def match(self, date: datetime.datetime) -> bool:
        return date.minute in self.__minutes

    def next(self, date: datetime.datetime) -> datetime.datetime:
        if date.minute >= self.__minutes[-1]:
            return datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=date.hour,
                minute=self.__minutes[0],
                tzinfo=date.tzinfo
            ) + datetime.timedelta(hours=1)

        for minute in self.__minutes:
            if date.minute < minute:
                return datetime.datetime(
                    year=date.year,
                    month=date.month,
                    day=date.day,
                    hour=date.hour,
                    minute=minute,
                    tzinfo=date.tzinfo
                )
