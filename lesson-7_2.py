from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def calc_consumption(self):
        pass


class Suit(Clothes):
    def __init__(self, size):
        Clothes.__init__(self, size)

    @property
    def calc_consumption(self):
        return 2 * self.size + 0.3


class Coat(Clothes):
    def __init__(self, size):
        Clothes.__init__(self, size)

    @property
    def calc_consumption(self):
        return self.size / 6.5 + 0.5


s1 = Suit(1.7)
print(s1.calc_consumption)

s2 = Coat(40)
print(s2.calc_consumption)