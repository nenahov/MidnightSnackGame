# Класс персонажа, у которого есть следующие поля: имя, пол, наличие предметов в инвентаре, здоровье, цель, текущее местоположение
class Person:
    """
    Класс игрового персонажа

    У него есть имя, текущее местоположение, предметы в инвентаре, цель и другие показатели.
    """

    def __init__(self, name: str, gender: str, inventory: set, health: int, goal: str, location: str):
        self.name = name
        self.gender = gender
        self.inventory = inventory
        self.health = health
        self.goal = goal
        self.location = location

    def __str__(self):
        return f"Name: {self.name}, Gender: {self.gender}, Inventory: {self.inventory}, Health: {self.health}, Goal: {self.goal}, Location: {self.location}"

    def __repr__(self):
        return f"Name: {self.name}, Gender: {self.gender}, Inventory: {self.inventory}, Health: {self.health}, Goal: {self.goal}, Location: {self.location}"
