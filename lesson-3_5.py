def sum_string_numbers(s):
    """
    Получает строку чисел и возвращает их сумму.

    :param s: строка чисел, разделенных пробелами
    :return: число
    """
    d_list = []
    for s in query.split():
        try:
            d_list.append(float(s))
        except ValueError:
            print(f"{s} - это не число. Игнорируем.")

    return sum(d_list)


s = 0
while True:
    query = input("Введите строку чисел, разделенных пробелами (пустая строка - звершение программы):")
    if len(query) == 0:
        break

    s += sum_string_numbers(query)
    print(f"Итоговая сумма: {s}")
