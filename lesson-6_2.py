class Road:
    __sqare_meter_mass = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_mass(self, thick):
        return self._length * self._width * Road.__sqare_meter_mass * thick


r = Road(length=5000, width=20)
print(r.count_mass(5))
