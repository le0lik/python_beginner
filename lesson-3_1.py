def my_div (devident, devider):
    """
    Делит devident на devider

    :param devident: int or float
    :param devider: int of float
    :return: float
    """
    if devider == 0:
        return

    return devident / devider


a = int(input("Введите делимое: "))
b = int(input("Введите делитель: "))

c = my_div(a, b)
if type(c) == type(None):
    print("Ошибка деления на ноль!")
else:
    print(f"{a} / {b} = {c}")
