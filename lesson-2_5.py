my_list = [7, 5, 3, 3, 2]
print(f"Изначальный рейтинг: {my_list}")
val = int(input("Новый элемент:"))
for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] >= val:
        i += 1
        break

my_list.insert(i, val)
print(f"Итоговы рейтинг: {my_list}")
