# Класс персонажа, у которого есть следующие поля: имя, пол, наличие предметов в инвентаре, здоровье, цель, текущее местоположение
class Person:
    def __init__(self, name, gender, inventory, health, goal, location):
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

