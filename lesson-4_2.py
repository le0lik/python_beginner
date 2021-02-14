def my_generator(o_list):
    """
    Возвращиает элементы исходного списка, значения которых больше предыдущего элемента

    :param o_list: list
    :return: iterator
    """
    for i in range(1, len(o_list)):
        if o_list[i] > o_list[i - 1]:
            yield o_list[i]


origin_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []

for i in my_generator(origin_list):
    new_list.append(i)

print(new_list)
