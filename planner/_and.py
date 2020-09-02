import datetime

from .aggregated_planning import AggregatedPlanning


class And(AggregatedPlanning):
    def match(self, date: datetime.datetime) -> bool:
        if len(self.plannings) == 0:
            raise RuntimeError('Empty And planning')

        for planning in self.plannings:
            if not planning.match(date):
                return False
        return True

    def next(self, date: datetime.datetime) -> datetime.datetime:
        if len(self.plannings) == 0:
            raise RuntimeError('Empty And planning')

        if len(self.plannings) == 1:
            return self.plannings[0].next(date)

        # If all the plannings match without without running next on them, we have to get the smallest next value and
        # start with that (otherwise it is not the next date but the current date
        if self.match(date):
            date = min(planning.next(date) for planning in self.plannings)

        while not self.match(date):
            date = max(planning.next(date) for planning in self.plannings if not planning.match(date))

        return date
