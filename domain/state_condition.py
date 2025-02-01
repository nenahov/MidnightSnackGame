# Класс, определяющий условия смены состояния персонажа и саму смену состояния.
# В условия входят
# - текущее расположение персонажа,
# - список предметов в инвентаре, хотя бы одна вещь должна быть для срабатывания условия
# - список предметов в инвентаре, которые должны быть все для срабатывания условия
# - список предметов в инвентаре, которые не должны быть для срабатывания условия
# Надпись для перехода в это состояние
# Выводимый на экран текст после перехода в это состояние
# Новое расположение персонажа после перехода в это состояние
# Новые предметы в инвентаре после перехода в это состояние
# Предметы, которые должны исчезнуть из инвентаря после перехода в это состояние
from domain.person import Person


class StateCondition:
    """
    Класс, определяющий условия смены состояния персонажа и саму смену состояния.

    У состояния есть:
        Надпись для перехода в это состояние
        Выводимый на экран текст после перехода в это состояние

    В условия входят:
        - текущее расположение персонажа,
        - список предметов в инвентаре, хотя бы одна вещь должна быть для срабатывания условия
        - список предметов в инвентаре, которые должны быть все для срабатывания условия
        - список предметов в инвентаре, которые не должны быть для срабатывания условия

    После применения этого перехода состояния у персонажа может измениться:
        - расположение персонажа
        - предметы в инвентаре
        - предметы, которые должны исчезнуть из инвентаря
    """
    def __init__(self,  order: int, id: str, name: str, location: str, items: set, all_items: set, not_items: set,
                 new_location: str, items_for_add: set, items_for_remove: set, text: str):
        self.order = order
        self.id = id
        self.name = name
        self.location = location
        self.items = items
        self.all_items = all_items
        self.not_items = not_items
        self.text = text
        self.new_location = new_location
        self.items_for_add = items_for_add
        self.items_for_remove = items_for_remove

    # Метод, который на вход принимает объект персонажа и на выход передает boolean значение, говорящее о том, срабатывает ли условие смены состояния
    def check_state_condition(self, person: Person) -> bool:
        return ((self.location is None or self.location == '' or self.location == person.location)
                and (len(self.items) == 0 or any(item in person.inventory for item in self.items))
                and (len(self.all_items) == 0 or all(item in person.inventory for item in self.all_items))
                and (len(self.not_items) == 0 or not any(item in person.inventory for item in self.not_items)))

    # Применяем новое состояние к персонажу
    def apply_state_condition(self, person: Person):
        # Сменить локацию, если она не пустая
        if self.new_location is not None and self.new_location != '':
            person.location = self.new_location
        person.inventory.update(self.items_for_add)
        person.inventory.difference_update(self.items_for_remove)
