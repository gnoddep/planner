import datetime

from .planning import Planning


class Hour(Planning):
    def __init__(self, hour: int):
        assert 1 <= hour <= 24
        self.__hour = hour

    @property
    def hour(self) -> int:
        return self.__hour

    def match(self, date: datetime.datetime) -> bool:
        return date.hour == self.__hour

    def next(self, date: datetime.datetime) -> datetime.datetime:
        if date.hour >= self.__hour:
            date += datetime.timedelta(days=1)
        return datetime.datetime(year=date.year, month=date.month, day=date.day, hour=self.__hour, tzinfo=date.tzinfo)
