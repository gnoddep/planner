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
        if date.hour < self.__hour:
            return date.replace(hour=self.__hour, minute=0, second=0, microsecond=0)
        else:
            return (date + datetime.timedelta(days=1)).replace(hour=self.__hour, minute=0, second=0, microsecond=0)
