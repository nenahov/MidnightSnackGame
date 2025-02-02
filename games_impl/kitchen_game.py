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

        if random.randint(0, 100) <= 50:
            # С вероятностью 50% оставляем фото либо в коридоре, либо на кухне
            person.inventory.add('pictureInCorridor')
        else:
            person.inventory.add('pictureInKitchen')

        # Случайный шифр из 4 неповторяющихся цифр
        digits = random.sample(range(10), 4)
        # Преобразуем список цифр в строку
        code = ''.join(map(str, digits))
        person.inventory.add('code=' + code)
        print(f"Шифр: {code}")
        return person

    def get_all_conditions(self) -> list[StateCondition]:
        return game_conditions

    def check_game_end(self, person: Person) -> str:
        if ('end' in person.inventory) or (person.health <= 0):
            res = ''
            if ('corridorLight' in person.inventory) or ('kitchenLight' in person.inventory):
                res += 'Ты забыл выключить свет!\n\n'
            if 'fridge' in person.inventory:
                res += ('Ты забыл закрыть холодильник!\n'
                        'Все продукты пропали!\n'
                        'Теперь надо что-то придумывать, что будет есть вся семья на завтрак!\n\n')
            res += 'Игра окончена 🏆'
            return res
        pass


game_conditions = [
    # Комната
    StateCondition(1, 'shoesOn', 'Надеть тапочки 🩰', 'Комната', set(), set(), {'shoes'},
                   '', {'shoes'}, set(), 'В тапочках тепло и уютно!\nМожно идти дальше'),

    StateCondition(1, 'shoesOff', 'Снять тапочки 🩰', 'Комната', set(), {'shoes'}, set(),
                   '', set(), {'shoes'}, 'Тапочки долой!'),

    StateCondition(10, 'corridor->room', 'Зайти в комнату 🚪', 'Коридор', set(), set(), set(),
                   'Комната', set(), set(), 'Теперь я в своей комнате'),

    StateCondition(10, 'room->corridorLightOn', 'Выйти в коридор 🚪', 'Комната', set(), set(), {'corridorLight'},
                   'Коридор', set(), set(), 'Теперь я в коридоре и тут очень темно 👀'),

    StateCondition(10, 'room->corridorLightOff', 'Выйти в коридор 🚪', 'Комната', set(), {'corridorLight'}, set(),
                   'Коридор', set(), set(), 'Теперь я в коридоре и тут кто-то забыл выключить свет 💡'),

    # лечь на кровать, если взяли сыр
    StateCondition(3, 'sleep', 'Поспать на кровати 🛌', 'Комната', {'cheese', 'meat', 'cake'}, set(), {'shoes'},
                   'Сновидения', set(), set(), 'Теперь я сытый и можно поспать! 😴'),

    # Лежать и видеть сны
    StateCondition(2, 'sleep1', 'Видеть сны 💤', 'Сновидения', {'cheese', 'picture'}, set(), {'meat'},
                   '', set(), set(), 'Снится замечательный сон! 😇'),

    StateCondition(2, 'sleep2', 'Видеть сны 💤', 'Сновидения', {'meat', 'picture'}, {'meat'}, set(),
                   '', set(), set(), 'Снится кошмар! 👹👻😓'),

    StateCondition(10, 'wakeUp', 'Проснуться ⏰', 'Сновидения', set(), set(), set(),
                   'Комната', {'end'}, set(), 'Проснулся в своей комнате ☀️'),

    # Коридор
    StateCondition(5, 'corridorLightOn', 'Включить свет в коридоре💡', 'Коридор', set(), set(), {'corridorLight'},
                   '', {'corridorLight'}, set(), 'Теперь светлее 💡. Можно идти дальше.'),

    StateCondition(5, 'corridorLightOff', 'Выключить свет в коридоре', 'Коридор', set(), {'corridorLight'}, set(),
                   '', set(), {'corridorLight'}, 'Опять темно 👀'),

    StateCondition(3, 'corridorLookAround', 'Осмотреться 👀', 'Коридор', set(), {'corridorLight'},
                   {'corridorLookAround'}, '', {'corridorLookAround'}, set(), 'Пока светло - осмотрелись в коридоре'),

    StateCondition(3, 'corridorFindPicture', 'Поднять листочек 🖼️', 'Коридор', set(),
                   {'pictureInCorridor', 'corridorLight', 'corridorLookAround'},
                   {'picture'}, '', {'picture'}, set(), 'Нашли прикольную фотку', '1.png'),

    StateCondition(5, 'kitchenLightOn', 'Включить свет на кухне 💡', 'Коридор', set(), set(), {'kitchenLight'},
                   '', {'kitchenLight'}, set(), 'Теперь на кухне светло 💡'),

    StateCondition(5, 'kitchenLightOff', 'Выключить свет на кухне', 'Коридор', set(), {'kitchenLight'}, set(),
                   '', set(), {'kitchenLight'}, 'На кухне темно'),

    StateCondition(10, 'corridor->kitchenLightOff', 'Зайти на кухню 🚪', 'Коридор', set(), set(), {'kitchenLight'},
                   'Кухня', set(), set(), 'Кухня! Тут темно. Где же этот холодильник?!'),

    StateCondition(10, 'corridor->kitchenLightOn', 'Зайти на кухню 🚪', 'Коридор', set(), {'kitchenLight'}, set(),
                   'Кухня', set(), set(), 'Кухня! Вот и холодильник! Можно и перекусить 🤤'),

    # Кухня

    # открыть холодильник
    StateCondition(3, 'openFridge', 'Открыть холодильник ❄️', 'Кухня', set(), {'kitchenLight'}, {'fridge'},
                   '', {'fridge'}, set(), 'Посмотрим, что тут есть вкусненького?! 🤤'),
    # Взять из холодильника сыр
    StateCondition(1, 'takeCheese', 'Сыр! 🧀', 'Кухня', set(), {'fridge'}, {'cheese'},
                   '', {'cheese'}, set(), 'Взяли сыр 🧀'),
    # кусок мяса
    StateCondition(1, 'takeMeat', 'Кусок мяса! 🍖', 'Кухня', set(), {'fridge'}, {'meat'},
                   '', {'meat'}, set(), 'Взяли кусок мяса! 🍖'),
    # Пирожное
    StateCondition(1, 'takeCake', 'Пирожное! 🍪', 'Кухня', set(), {'fridge'}, {'cake'},
                   '', {'cake'}, set(), 'Взяли пирожное! 🍪'),
    # закрыть холодильник
    StateCondition(3, 'closeFridge', 'Закрыть холодильник ❄️', 'Кухня', set(), {'fridge'}, set(),
                   '', set(), {'fridge'}, 'Итак, я посреди кухни. Что делаем дальше?'),

    StateCondition(3, 'kitchenLookAround', 'Осмотреться 👀', 'Кухня', set(), {'kitchenLight'},
                   {'kitchenLookAround'}, '', {'kitchenLookAround'}, set(), 'Пока светло - осмотрелись на кухне'),

    StateCondition(3, 'kitchenFindPicture', 'Поднять листочек 🖼️', 'Кухня', set(),
                   {'pictureInKitchen', 'kitchenLight', 'kitchenLookAround'}, {'picture'}, '', {'picture'}, set(),
                   'Нашли прикольную фотку', '1.png'),

    # из кухни в коридор
    StateCondition(10, 'kitchen->corridorLightOn', 'Выйти в коридор 🚪', 'Кухня', set(), set(), {'corridorLight'},
                   'Коридор', set(), set(), 'Теперь я в коридоре и тут очень темно 👀'),

    StateCondition(10, 'kitchen->corridorLightOff', 'Выйти в коридор 🚪', 'Кухня', set(), {'corridorLight'}, set(),
                   'Коридор', set(), set(), 'Теперь я в коридоре и тут светло 💡'),
]
