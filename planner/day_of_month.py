import calendar
import datetime

from .planning import Planning


class DayOfMonth(Planning):
    FIRST = 1
    LAST = 0

    def __init__(self, day_of_month: int):
        if (day_of_month < 1 or day_of_month > 31) and day_of_month != self.LAST:
            raise ValueError('day_of_month must be from 1 to 31')
        self.__day_of_month = day_of_month

    @property
    def day_of_month(self) -> int:
        return self.__day_of_month

    def match(self, date: datetime.datetime) -> bool:
        return date.day == self.__get_day_of_month(date)

    def next(self, date: datetime.datetime) -> datetime.datetime:
        day_of_month = self.__get_day_of_month(date)
        if date.day < day_of_month <= self.__get_last_day_of_month(date):
            return date.replace(day=day_of_month, hour=0, minute=0, second=0, microsecond=0)

        date = self.__next_month(date.replace(day=1))
        while self.__day_of_month > self.__get_last_day_of_month(date):
            date = self.__next_month(date)

        return date.replace(day=self.__get_day_of_month(date), hour=0, minute=0, second=0, microsecond=0)

    def __get_day_of_month(self, date: datetime.datetime) -> int:
        if self.__day_of_month == self.LAST:
            return self.__get_last_day_of_month(date)
        return self.__day_of_month

    @staticmethod
    def __get_last_day_of_month(date: datetime.datetime) -> int:
        return calendar.monthrange(date.year, date.month)[1]

    @staticmethod
    def __next_month(date: datetime.datetime) -> datetime.datetime:
        if date.month == 12:
            return date.replace(year=date.year + 1, month=1)
        return date.replace(month=date.month + 1)
