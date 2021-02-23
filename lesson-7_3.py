class Cell:
    def __init__(self, count):
        if not isinstance(count, int):
            raise ValueError("count must be Int")
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if other.count >= self.count:
            raise ValueError("Not enough cells")

        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(int(self.count // other.count))

    def make_order(self, n):
        if not isinstance(n, int):
            raise ValueError("count must be Int")

        s = ""
        x = int(self.count // n)
        for i in range(x):
            for j in range(n):
                s += "*"
            s += "\n"
        y = self.count % n
        if y > 0:
            for j in range(y):
                s += "*"
        return s


c1 = Cell(10)
c2 = Cell(14)

print((c1 + c2).make_order(5))