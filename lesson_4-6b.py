from itertools import cycle
origin_list = [3, 4, 10]
stop_count = 10

def my_iterator(orig, cnt):
    """
    Возвращает итератор повторяющий значения из списка <orig> <cnt> раз

    :param orig: list
    :param cnt: int
    :return: iterator
    """
    c = 0
    for i in cycle(orig):
        c += 1
        if c > cnt:
            return
        else:
            yield i


new_list = [i for i in my_iterator(origin_list, stop_count)]

print(new_list)