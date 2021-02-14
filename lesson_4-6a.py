from itertools import count
start_number = 3
stop_number = 10

# XXX:
# new_list = [i for i in count(start_number) if i <= stop_number]


def my_iterator(start, stop):
    """
    Возвращает итератор от start до stop

    :param start: int
    :param stop: int
    :return: iterator
    """
    for i in count(start):
        if i > stop:
            return
        else:
            yield i


new_list = [i for i in my_iterator(start_number, stop_number)]

print(new_list)