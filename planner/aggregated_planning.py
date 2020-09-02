from typing import List

from .planning import Planning


class AggregatedPlanning(Planning):
    def __init__(self, *plannings: Planning):
        self.__plannings: List[Planning] = list(plannings)

    def add(self, planning: Planning) -> None:
        self.__plannings.append(planning)

    @property
    def plannings(self) -> List[Planning]:
        return self.__plannings
