class Stationery:
    title = ""

    def __init__(self):
        Stationery.title = "Stationery"

    def draw(self):
        print("Запуск отрисовки.")
        print(Stationery.title)


class Pencil(Stationery):
    def __init__(self):
        Pencil.title = "Pencil"

    def draw(self):
        print("Запуск отрисовки Каранндашом.")
        print(Pencil.title)

class Pen(Stationery):
    def __init__(self):
        Pen.title = "Pen"

    def draw(self):
        print("Запуск отрисовки Ручкой.")
        print(Pen.title)


class Handle(Stationery):
    def __init__(self):
        Handle.title = "Handle"

    def draw(self):
        print("Запуск отрисовки Маркером.")
        print(Handle.title)


p1 = Pencil()
p1.draw()

p2 = Pen()
p3 = Handle()

p1.draw()
p2.draw()
p3.draw()

p4 = Handle()
p4.draw()

p3.draw()
p4.draw()
