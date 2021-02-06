def int_func(text):
    """
    Преобразует первую букву строки в заглавную

    :param text: строка
    :return: строка
    """
    #return text.capitalize()
    t = bytearray(text, "latin_1");
    if t[0] >= 0x61 and t[0] <= 0x7A:
        t[0] -= 0x20
    return t.decode()


query = "one two three four five"

l = []
for s in query.split():
    l.append(int_func(s))

result = " ".join(l)

print(result)


