import os
from textx import metamodel_from_file
from typing import List, Optional

from .planning import Planning
from . import And, Or, Month, DayOfMonth, Hour

_MONTHS = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12,
}


class Parser(object):
    def __init__(self):
        self.__meta_model = metamodel_from_file(
            os.path.dirname(__file__) + '/planner.tx',
            use_regexp_group=True,
            ignore_case=True
        )

    def parse(self, planning_str: str) -> Optional[Planning]:
        model = self.__meta_model.model_from_str(planning_str)

        plannings: List[Planning] = []

        if model.of_month is not None:
            plannings.append(self.__of_month(model.of_month))

        if model.at_time is not None:
            plannings.append(Hour(int(model.at_time.time.hour)))

        if len(plannings) == 1:
            return plannings[0]

        return And(*plannings)

    @staticmethod
    def __of_month(of_month) -> Planning:
        planning = None

        if of_month.months.every_month:
            if of_month.day_of_month is None:
                planning = Or(*[Month(month) for month in _MONTHS.values()])
        else:
            if len(of_month.months.months) == 1:
                planning = Month(_MONTHS[of_month.months.months[0].lower()])
            elif not of_month.months.every_month:
                planning = Or()
                for month in of_month.months.months:
                    planning.add(Month(_MONTHS[month.lower()]))

        if of_month.day_of_month is not None:
            if planning:
                planning = And(planning, DayOfMonth(int(of_month.day_of_month)))
            else:
                planning = DayOfMonth(int(of_month.day_of_month))

        return planning
