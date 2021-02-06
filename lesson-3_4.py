def my_func1(x, y):
    """
    Возводит х в степень у

    :param x: число
    :param y: число
    :return: число
    """
    return x ** y


def my_func2(x, y):
    """
    Возводит х в степень у

    :param x: число
    :param y: отрицательное число
    :return: число или None
    """
    if y >= 0:
        return None

    res = 1 / x
    tmp = abs(y)

    while tmp > 1:
        res /= x
        tmp -= 1

    return res


def my_func3(x, y):
    """
    Возводит х в степень у

    :param x: число
    :param y: число
    :return: число
    """
    if y == 0:
        return 1

    res = x
    tmp = abs(y)

    while tmp > 1:
        res *= x
        tmp -= 1

    if y < 0:
        res = 1 / res

    return res


print(my_func1(2, -3))
print(my_func2(2, -3))
print(my_func3(2, -3))
