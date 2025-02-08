from abc import ABC, abstractmethod

from domain.person import Person
from domain.state_condition import StateCondition


class AbstractGame(ABC):

    @abstractmethod
    def create_person(self) -> Person:
        # return Person('София', 'Женский', {"София"}, 100, 'Утолить голод', 'Комната')
        pass

    @abstractmethod
    def check_game_end(self, person: Person) -> str:
        pass

    @abstractmethod
    def get_person_inventory_description(self, person: Person) -> str:
        pass

    @abstractmethod
    def get_all_conditions(self) -> list[StateCondition]:
        pass

    def get_conditions_for_person(self, person: Person) -> list[StateCondition]:
        return [condition for condition in self.get_all_conditions() if condition.check_state_condition(person)]

    def get_condition_by_id(self, id: str, person: Person) -> StateCondition:
        for condition in self.get_all_conditions():
            if condition.id == id and condition.check_state_condition(person):
                return condition
