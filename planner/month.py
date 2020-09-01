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
            return datetime.datetime(year=date.year, month=self.__month, day=1, tzinfo=date.tzinfo)
        return datetime.datetime(year=date.year + 1, month=self.__month, day=1, tzinfo=date.tzinfo)
