"""
Задание 3.
Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = 'Tom'
    surname = 'Sandler'
    position = 'Seller'

    def __init__(self, wage, bonus):
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return int(self._income['wage'])+int(self._income['bonus'])


a = Position('500', '100')
print("Проверка атрибутов:")
print(f"position is: {a.position}")
print(f"name is: {a.name}")
print(f"surname is: {a.surname}")
print("Проверка вызова методов экземпляра: ")
print(f"full name is: {a.get_full_name()}")
print(F"Total income is: {a.get_total_income()}")
