from abc import ABC, abstractmethod
from domain.state_condition import StateCondition
from domain.person import Person


class AbstractGame(ABC):

    @abstractmethod
    def create_person(self):
        # return Person('София', 'Женский', {"София"}, 100, 'Утолить голод', 'Комната')
        pass

    @abstractmethod
    def get_all_conditions(self):
        pass

    def get_conditions_for_person(self, person):
        return [condition for condition in self.get_all_conditions() if condition.check_state_condition(person)]

    def get_condition_by_id(self, id, person):
        for condition in self.get_all_conditions():
            if condition.id == id and condition.check_state_condition(person):
                return condition