"""
Задание 4.
Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
speed, color, name, is_police (булево).
А также публичные методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс публичный метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, flag):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = flag

    def go(self):
        if self.speed == 0:
            print(f"Машина {self.name} остановилась")
        else:
            print(f"Машина {self.name} едет")

    def stop(self):
        if self.speed == 0:
            print(f"Машина {self.name} остановилась")
        else:
            print(f"Машина {self.name} едет")

    def turn(self, direction):
        if direction == "налево" or direction == "направо" or direction == "назад":
            print(f"Машина {self.name} повернула {direction}.")
        else:
            print(f"Машина {self.name} продолжает ехать прямо.")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} в классе Car: {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, flag):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = flag

    def show_speed(self):
        if self.speed > 60:
            print("Вы превысили сокрость!")
        else:
            print(
                f"Текущая скорость автомобиля {self.name} в классе TownCar: {self.speed}"
            )


class SportCar(Car):
    def __init__(self, speed, color, name, flag):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = flag


class WorkCar(Car):
    def __init__(self, speed, color, name, flag):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = flag

    def show_speed(self):
        if self.speed > 40:
            print("Вы превысили скорость!")
        else:
            print(f"Текущая скорость автомобиля в классе WorkCar: {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name, flag):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = flag


a_base = Car("60", " ", "bmw", False)
print(f"Текущая скорость автомобиля:{a_base.speed}")
a_base.show_speed()
a_base.stop()

b_town = TownCar("40", "green", "cooper", False)
b_town.show_speed()
print(b_town.go())

c_work = WorkCar("30", "green", "Lada", False)
c_work.show_speed()
c_work.turn("прямо")

d_police = PoliceCar("50", "red", "bmw", True)
print(f"Машина {d_police.name} является полицейской? {d_police.is_police}")
