def my_func(a, b, c):
    """
    Возвращает сумму двух наибольших аргументов

    :param a: число или строка
    :param b: число или строка
    :param c: число или строка
    :return: число или строка
    """
    l = [a, b, c]
    l.remove(min(l))
    return l[0] + l[1]


print(my_func(10, 12, 8))
print(my_func("qw", "we", "e"))
