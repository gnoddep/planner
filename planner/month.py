import datetime

from .planning import Planning


class Month(Planning):
    def __init__(self, month: int):
        assert 1 <= month <= 12
        self.__month = month

    @property
    def hour(self) -> int:
        return self.__month

    def match(self, date: datetime.datetime) -> bool:
        return date.month == self.__month

    def next(self, date: datetime.datetime) -> datetime.datetime:
        if date.month < self.__month:
            return date.replace(month=self.__month, day=1, hour=0, minute=0, second=0, microsecond=0)
        return date.replace(year=date.year + 1, month=self.__month, day=1, hour=0, minute=0, second=0, microsecond=0)
