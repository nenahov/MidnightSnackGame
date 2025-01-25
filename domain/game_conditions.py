# Есть класс
# # Класс, определяющий условия смены состояния персонажа и саму смену состояния.
# # В условия входят
# # - текущее расположение персонажа,
# # - список предметов в инвентаре, хотя бы одна вещь должна быть для срабатывания условия
# # - список предметов в инвентаре, которые должны быть все для срабатывания условия
# # - список предметов в инвентаре, которые не должны быть для срабатывания условия
# # Надпись для перехода в это состояние
# # Выводимый на экран текст после перехода в это состояние
# # Новое расположение персонажа после перехода в это состояние
# # Новые предметы в инвентаре после перехода в это состояние
# # Предметы, которые должны исчезнуть из инвентаря после перехода в это состояние
#
# class StateCondition:
# def __init__(self, id, name, location, items, all_items, not_items, new_location, items_for_add, items_for_remove,
#              text):
#     self.id = id
#     self.name = name
#     self.location = location
#     self.items = items
#     self.all_items = all_items
#     self.not_items = not_items
#     self.text = text
#     self.new_location = new_location
#     self.items_for_add = items_for_add
#     self.items_for_remove = items_for_remove
from domain.state_condition import StateCondition

# Определим список состояний:
# - Тапочки: текущее расположение - комната, Надпись для перехода - Надеть тапочки, Выводимый на экран текст: Теперь можно отправляться в путь, новый предмет в инвентаре - тапочки
# - Коридор из комнаты: текущее расположение - комната, необходимые вещи в инвентаре - тапочки, Надпись - выйти в коридор, текст - мы пришли в коридор, новое расположение - коридор

game_conditions = [
    # Комната
    StateCondition("shoesOn", "Надеть тапочки", "Комната", {}, {}, {"shoes"},
                   None, {"shoes"}, {}, "В тапочках тепло и уютно!\nМожно идти дальше"),

    StateCondition("shoesOff", "Снять тапочки", "Комната", {}, {"shoes"}, {"corridorLight"},
                   None, {}, {"shoes"}, "Можно полежать на кровати! 😴"),

    StateCondition("corridor->room", "Зайти в комнату", "Коридор", {}, {}, {},
                   "Комната", {}, {}, "Теперь я в своей комнате"),

    StateCondition("room->corridorLightOn", "Выйти в коридор", "Комната", {}, {}, {"corridorLight"},
                   "Коридор", {}, {}, "Теперь я в коридоре и тут очень темно 👀"),

    StateCondition("room->corridorLightOff", "Выйти в коридор", "Комната", {}, {"corridorLight"}, {},
                   "Коридор", {}, {}, "Теперь я в коридоре и тут кто-то забыл выключить свет 💡"),

    # Коридор
    StateCondition("corridorLightOn", "Включить свет 💡", "Коридор", {}, {}, {"corridorLight"},
                   None, {"corridorLight"}, {}, "Теперь светлее 💡. Можно идти дальше."),

    StateCondition("corridorLightOff", "Выключить свет", "Коридор", {}, {"corridorLight"}, {},
                   None, {}, {"corridorLight"}, "Опять темно 👀"),

    StateCondition("corridor->kitchen", "Зайти на кухню", "Коридор", {}, {}, {"kitchenLight"},
                   "Кухня", {}, {}, "Кухня! Тут темно. Где же этот холодильник?!"),

    StateCondition("corridor->kitchen", "Зайти на кухню", "Коридор", {}, {"kitchenLight"}, {},
                   "Кухня", {}, {}, "Кухня! Вот и холодильник! Можно и перекусить 🤤"),

    # Кухня

    # открыть холодильник
    StateCondition("openFridge", "Открыть холодильник", "Кухня", {}, {}, {"fridge"},
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

    StateCondition("kitchenLightOn", "Включить свет", "Кухня", {}, {}, {"kitchenLight"},
                   None, {"kitchenLight"}, {}, "Теперь светлее.  Вот и холодильник! Можно и перекусить 🤤"),

    StateCondition("kitchenLightOff", "Выключить свет", "Кухня", {}, {"kitchenLight"}, {},
                   None, {}, {"kitchenLight"}, "Опять темно"),

    # из кухни в коридор
    StateCondition("kitchen->corridorLightOn", "Выйти в коридор", "Кухня", {}, {}, {"corridorLight"},
                   "Коридор", {}, {}, "Теперь я в коридоре и тут очень темно 👀"),

    StateCondition("kitchen->corridorLightOff", "Выйти в коридор", "Кухня", {}, {"corridorLight"}, {},
                   "Коридор", {}, {}, "Теперь я в коридоре и тут светло 💡"),
]
