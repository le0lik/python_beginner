from math import factorial


def fact(n):
    """
    Возвращает итератор чисел от 1! до n!

    :param n: int
    :return: iterator
    """
    for i in range(1, n + 1):
        yield factorial(i)


for el in fact(4):
    print(el)
