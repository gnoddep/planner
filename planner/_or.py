import datetime

from .planning import Planning


class Or(Planning):
    def __init__(self, *plannings: Planning):
        self.__plannings = plannings

    def match(self, date: datetime.datetime) -> bool:
        for planning in self.__plannings:
            if planning.match(date):
                return True
        return False

    def next(self, date: datetime.datetime) -> datetime.datetime:
        dates = []
        for planning in self.__plannings:
            dates.append(planning.next(date))
        return min(dates)
