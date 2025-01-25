import random

from domain.abstract_game import AbstractGame
from domain.person import Person
from domain.state_condition import StateCondition


class KitchenGame(AbstractGame):

    def create_person(self) -> Person:
        person = Person('София', 'Женский', {'София'}, 100, 'Утолить голод', 'Комната')
        if random.randint(0, 100) <= 20:
            # С вероятностью 20% включим свет в коридоре
            person.inventory.add('corridorLight')
        return person

    def get_all_conditions(self) -> list[StateCondition]:
        return game_conditions

    def check_game_end(self, person: Person) -> str:
        if ('end' in person.inventory) or (person.health <= 0):
            return 'Игра окончена'
        pass


game_conditions = [
    # Комната
    StateCondition('shoesOn', 'Надеть тапочки', 'Комната', set(), set(), {'shoes'},
                   '', {'shoes'}, set(), 'В тапочках тепло и уютно!\nМожно идти дальше'),

    StateCondition('shoesOff', 'Снять тапочки', 'Комната', set(), {'shoes'}, {'corridorLight'},
                   '', set(), {'shoes'}, 'Тапочки долой!'),

    StateCondition('corridor->room', 'Зайти в комнату', 'Коридор', set(), set(), set(),
                   'Комната', set(), set(), 'Теперь я в своей комнате'),

    StateCondition('room->corridorLightOn', 'Выйти в коридор', 'Комната', set(), set(), {'corridorLight'},
                   'Коридор', set(), set(), 'Теперь я в коридоре и тут очень темно 👀'),

    StateCondition('room->corridorLightOff', 'Выйти в коридор', 'Комната', set(), {'corridorLight'}, set(),
                   'Коридор', set(), set(), 'Теперь я в коридоре и тут кто-то забыл выключить свет 💡'),

    # лечь на кровать, если взяли сыр
    StateCondition('sleep', 'Поспать на кровати', 'Комната', set(), {'cheese'}, {'shoes'},
                   'Сновидения', set(), set(), 'Теперь я сытый и можно поспать! 😴'),

    # Лежать и видеть сны
    StateCondition('sleep1', 'Видеть сны', 'Сновидения', {'cheese'}, set(), {'meat'},
                   '', set(), set(), 'Снится замечательный сон! 😇'),

    StateCondition('sleep2', 'Видеть сны', 'Сновидения', {'meat'}, set(), set(),
                   '', set(), set(), 'Снится кошмар! 👹👻😓'),

    StateCondition('wakeUp', 'Проснуться', 'Сновидения', set(), set(), set(),
                   'Комната', {'end'}, set(), 'Проснулся в своей комнате'),

    # Коридор
    StateCondition('corridorLightOn', 'Включить свет в коридоре💡', 'Коридор', set(), set(), {'corridorLight'},
                   '', {'corridorLight'}, set(), 'Теперь светлее 💡. Можно идти дальше.'),

    StateCondition('corridorLightOff', 'Выключить свет в коридоре', 'Коридор', set(), {'corridorLight'}, set(),
                   '', set(), {'corridorLight'}, 'Опять темно 👀'),

    StateCondition('kitchenLightOn', 'Включить свет на кухне 💡', 'Коридор', set(), set(), {'kitchenLight'},
                   '', {'kitchenLight'}, set(), 'Теперь на кухне светло 💡'),

    StateCondition('kitchenLightOff', 'Выключить свет на кухне', 'Коридор', set(), {'kitchenLight'}, set(),
                   '', set(), {'kitchenLight'}, 'На кухне темно'),

    StateCondition('corridor->kitchenLightOff', 'Зайти на кухню', 'Коридор', set(), set(), {'kitchenLight'},
                   'Кухня', set(), set(), 'Кухня! Тут темно. Где же этот холодильник?!'),

    StateCondition('corridor->kitchenLightOn', 'Зайти на кухню', 'Коридор', set(), {'kitchenLight'}, set(),
                   'Кухня', set(), set(), 'Кухня! Вот и холодильник! Можно и перекусить 🤤'),

    # Кухня

    # открыть холодильник
    StateCondition('openFridge', 'Открыть холодильник', 'Кухня', set(), {'kitchenLight'}, {'fridge'},
                   '', {'fridge'}, set(), 'Посмотрим, что тут есть вкусненького?! 🤤'),

    # Взять из холодильника сыр
    StateCondition('takeCheese', 'Сыр! 🧀', 'Кухня', set(), {'fridge'}, {'cheese'},
                   '', {'cheese'}, set(), 'Взяли сыр 🧀'),
    # кусок мяса
    StateCondition('takeMeat', 'Кусок мяса! 🍖', 'Кухня', set(), {'fridge'}, {'meat'},
                   '', {'meat'}, set(), 'Взяли кусок мяса! 🍖'),

    # Пирожное
    StateCondition('takeCake', 'Пирожное! 🍪', 'Кухня', set(), {'fridge'}, {'cake'},
                   '', {'cake'}, set(), 'Взяли пирожное! 🍪'),

    # закрыть холодильник
    StateCondition('closeFridge', 'Закрыть холодильник', 'Кухня', set(), {'fridge'}, set(),
                   '', set(), {'fridge'}, 'Итак, я посреди кухни. Что делаем дальше?'),

    # из кухни в коридор
    StateCondition('kitchen->corridorLightOn', 'Выйти в коридор', 'Кухня', set(), set(), {'corridorLight'},
                   'Коридор', set(), set(), 'Теперь я в коридоре и тут очень темно 👀'),

    StateCondition('kitchen->corridorLightOff', 'Выйти в коридор', 'Кухня', set(), {'corridorLight'}, set(),
                   'Коридор', set(), set(), 'Теперь я в коридоре и тут светло 💡'),
]
