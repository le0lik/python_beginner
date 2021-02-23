class Car:
    def __init__(self, name, color):
        self.color = color
        self.name = name
        self.speed = 0
        self.is_police = False
        self.type = ''

    def go(self, speed):
        self.speed = speed
        print(f"Машина {self.type} едет со скоростью {self.speed} км/ч")

    def stop(self):
        self.speed = 0
        print(f"Машина {self.type} остановилась")

    def turn(self, direction):
        print(f"Машина {self.type} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.type} {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, name, color):
        Car.__init__(self, name, color)
        self.type = "TownCar"

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print(f"Превышение скорости для {self.type}!")


class SportCar(Car):
    def __init__(self, name, color):
        Car.__init__(self, name, color)
        self.type = "SportCar"


class WorkCar(Car):
    def __init__(self, name, color):
        Car.__init__(self, name, color)
        self.type = "WorkCar"

    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print(f"Превышение скорости для {self.type}!")


class PoliceCar(Car):
    def __init__(self, name, color):
        Car.__init__(self, name, color)
        self.type = "PoliceCar"
        self.is_police = True


c1 = SportCar('Nissan', 'Yellow')
c2 = TownCar('Lincoln', 'White')

c1.go(300)
c2.go(10)

c1.show_speed()

c2.speed = 100
c2.show_speed()