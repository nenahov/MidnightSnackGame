import random

from domain.abstract_game import AbstractGame
from domain.person import Person
from domain.state_condition import StateCondition


class KitchenGame(AbstractGame):

    def create_person(self):
        person = Person('София', 'Женский', {"София"}, 100, 'Утолить голод', 'Комната')
        # В цикле от 1 до 100 с шагом 10 генерим случайное число
        for i in range(0, 100, 10):
            random_number = random.randint(0, 100)
            # Если число больше 50
            if i >= random_number:
                # Добавляем предмет в инвентарь
                person.inventory.add(f'random{i}')
        return person

    def get_all_conditions(self):
        return game_conditions


game_conditions = [
    # Комната
    StateCondition("shoesOn", "Надеть тапочки", "Комната", {}, {}, {"shoes"},
                   None, {"shoes"}, {}, "В тапочках тепло и уютно!\nМожно идти дальше"),

    StateCondition("shoesOff", "Снять тапочки", "Комната", {}, {"shoes"}, {"corridorLight"},
                   None, {}, {"shoes"}, "Тапочки долой!"),

    StateCondition("corridor->room", "Зайти в комнату", "Коридор", {}, {}, {},
                   "Комната", {}, {}, "Теперь я в своей комнате"),

    StateCondition("room->corridorLightOn", "Выйти в коридор", "Комната", {}, {}, {"corridorLight"},
                   "Коридор", {}, {}, "Теперь я в коридоре и тут очень темно 👀"),

    StateCondition("room->corridorLightOff", "Выйти в коридор", "Комната", {}, {"corridorLight"}, {},
                   "Коридор", {}, {}, "Теперь я в коридоре и тут кто-то забыл выключить свет 💡"),

    # лечь на кровать, если взяли сыр
    StateCondition("sleep", "Поспать на кровати", "Комната", {}, {"cheese"}, {"shoes"},
                   "Сновидения", {}, {}, "Теперь я сытый и можно поспать! 😴"),

    # Лежать и видеть сны
    StateCondition("sleep1", "Видеть сны", "Сновидения", {"cheese"}, {}, {"meat"},
                   None, {}, {}, "Снится замечательный сон! 😇"),

    StateCondition("sleep2", "Видеть сны", "Сновидения", {"meat"}, {}, {},
                   None, {}, {}, "Снится кошмар! 👹👻😓"),

    StateCondition("wakeUp", "Проснуться", "Сновидения", {}, {}, {},
                   "Комната", {}, {}, "Проснулся в своей комнате"),

    # Коридор
    StateCondition("corridorLightOn", "Включить свет в коридоре💡", "Коридор", {}, {}, {"corridorLight"},
                   None, {"corridorLight"}, {}, "Теперь светлее 💡. Можно идти дальше."),

    StateCondition("corridorLightOff", "Выключить свет в коридоре", "Коридор", {}, {"corridorLight"}, {},
                   None, {}, {"corridorLight"}, "Опять темно 👀"),

    StateCondition("kitchenLightOn", "Включить свет на кухне 💡", "Коридор", {}, {}, {"kitchenLight"},
                   None, {"kitchenLight"}, {}, "Теперь на кухне светло 💡"),

    StateCondition("kitchenLightOff", "Выключить свет на кухне", "Коридор", {}, {"kitchenLight"}, {},
                   None, {}, {"kitchenLight"}, "На кухне темно"),

    StateCondition("corridor->kitchenLightOff", "Зайти на кухню", "Коридор", {}, {}, {"kitchenLight"},
                   "Кухня", {}, {}, "Кухня! Тут темно. Где же этот холодильник?!"),

    StateCondition("corridor->kitchenLightOn", "Зайти на кухню", "Коридор", {}, {"kitchenLight"}, {},
                   "Кухня", {}, {}, "Кухня! Вот и холодильник! Можно и перекусить 🤤"),

    # Кухня

    # открыть холодильник
    StateCondition("openFridge", "Открыть холодильник", "Кухня", {}, {"kitchenLight"}, {"fridge"},
                   None, {"fridge"}, {}, "Посмотрим, что тут есть вкусненького?! 🤤"),

    # Взять из холодильника сыр
    StateCondition("takeCheese", "Сыр! 🧀", "Кухня", {}, {"fridge"}, {"cheese"},
                   None, {"cheese"}, {}, "Взяли сыр 🧀"),
    # кусок мяса
    StateCondition("takeMeat", "Кусок мяса! 🍖", "Кухня", {}, {"fridge"}, {"meat"},
                   None, {"meat"}, {}, "Взяли кусок мяса! 🍖"),

    # Пирожное
    StateCondition("takeCake", "Пирожное! 🍪", "Кухня", {}, {"fridge"}, {"cake"},
                   None, {"cake"}, {}, "Взяли пирожное! 🍪"),

    # закрыть холодильник
    StateCondition("closeFridge", "Закрыть холодильник", "Кухня", {}, {"fridge"}, {},
                   None, {}, {"fridge"}, "Итак, я посреди кухни. Что делаем дальше?"),

    # из кухни в коридор
    StateCondition("kitchen->corridorLightOn", "Выйти в коридор", "Кухня", {}, {}, {"corridorLight"},
                   "Коридор", {}, {}, "Теперь я в коридоре и тут очень темно 👀"),

    StateCondition("kitchen->corridorLightOff", "Выйти в коридор", "Кухня", {}, {"corridorLight"}, {},
                   "Коридор", {}, {}, "Теперь я в коридоре и тут светло 💡"),
]
