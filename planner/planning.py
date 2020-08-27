import abc
import datetime


class Planning(abc.ABC):
    @abc.abstractmethod
    def match(self, date: datetime.datetime) -> bool:
        pass

    @abc.abstractmethod
    def next(self, date: datetime.datetime) -> datetime.datetime:
        pass
