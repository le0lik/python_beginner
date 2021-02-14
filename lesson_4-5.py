from functools import reduce

new_list = [el for el in range(100, 10001, 2)]
print(reduce(lambda p_1, p_2: p_1 * p_2, new_list))
