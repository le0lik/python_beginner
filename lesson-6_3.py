class Worker:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.position = ""
        self._income = {"wage": 0, "bonus": 0}


class Position(Worker):

    def get_full_name(self):
        return " ".join((self.name, self.surname))

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


p = Position()
p.surname = "Иванов"
p.name = "Иван"
p.position = 'Гуру'
p._income = {"wage": 12000, "bonus": 3400}

print(p.get_full_name())
print(p.get_total_income())
