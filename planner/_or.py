import datetime

from .aggregated_planning import AggregatedPlanning


class Or(AggregatedPlanning):
    def match(self, date: datetime.datetime) -> bool:
        if len(self.plannings) == 0:
            raise RuntimeError('Empty Or planning')

        for planning in self.plannings:
            if planning.match(date):
                return True
        return False

    def next(self, date: datetime.datetime) -> datetime.datetime:
        if len(self.plannings) == 0:
            raise RuntimeError('Empty Or planning')

        dates = []
        for planning in self.plannings:
            dates.append(planning.next(date))
        return min(dates)
