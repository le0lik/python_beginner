origin_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in origin_list if origin_list.count(el) == 1]
print(new_list)
