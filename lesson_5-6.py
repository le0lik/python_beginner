filename = "lesson-5_6.txt"


def str_to_int(s):
    """
    Преобразует строку в целое число, игнорируя символы не являющиеся числами

    :param s: string
    :return: int
    """
    tmp = ""

    for i in s:
        if i.isdigit():
            tmp += i

    if tmp == "":
        return 0
    else:
        return int(tmp)


result_dict = {}

with open(filename, encoding="UTF8") as txtfile:
    for line in txtfile:
        lesson = line.strip().split(" ")
        result_dict[lesson[0].rstrip(':')] = str_to_int(lesson[1]) + \
                                             str_to_int(lesson[2]) + \
                                             str_to_int(lesson[3])

print(result_dict)
