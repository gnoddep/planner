import datetime

from .planning import Planning


class And(Planning):
    def __init__(self, planning: Planning, *plannings: Planning):
        self.__plannings = [planning] + list(plannings)

    def match(self, date: datetime.datetime) -> bool:
        for planning in self.__plannings:
            if not planning.match(date):
                return False
        return True

    def next(self, date: datetime.datetime) -> datetime.datetime:
        if len(self.__plannings) == 1:
            return self.__plannings[0].next(date)

        prev_latest_date_idx = None
        dates = [date] * len(self.__plannings)

        while True:
            latest_date_idx = None
            for idx, planning in enumerate(self.__plannings):
                if prev_latest_date_idx is not None and planning.match(dates[prev_latest_date_idx]):
                    continue

                dates[idx] = planning.next(dates[idx])

                if latest_date_idx is None or dates[idx] > dates[latest_date_idx]:
                    latest_date_idx = idx

            if prev_latest_date_idx is None or dates[latest_date_idx] > dates[prev_latest_date_idx]:
                prev_latest_date_idx = latest_date_idx

            if self.match(dates[prev_latest_date_idx]):
                return dates[prev_latest_date_idx]
