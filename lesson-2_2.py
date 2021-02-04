tmp_list = []

while True:
    val = input("Введите элемент списка (пустая строка - конец ввода):")
    if val == "":
        break
    tmp_list.append(val)

print(f"Исходный список: {tmp_list}")

for i in range(0, len(tmp_list) - 1, 2):
    (tmp_list[i], tmp_list[i + 1]) = (tmp_list[i + 1], tmp_list[i])

print(f"Итоговый список: {tmp_list}")
