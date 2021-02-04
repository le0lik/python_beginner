products = []
n = abs(int(input("Введите количество товаров:")))

for i in range(1, n + 1):
    name = input(f"[товар {i} из {n}] Название:")
    prise = abs(float(input(f"[товар {i} из {n}] Цена:")))
    count = abs(int(input(f"[товар {i} из {n}] Количество:")))
    metric = input(f"[товар {i} из {n}] Единица измерения:")
    products.append((i, {"название": name, "цена": prise, "количество": count, "ед": metric}))
    print()

# make product matrix
matrix = []
for p in products:
    (i, d) = p
    matrix.append(tuple(d.values()))

tmp_list = list(zip(*matrix))
analytics = {"название": list(set(tmp_list[0])), \
             "цена": list(set(tmp_list[1])), \
             "количество": list(set(tmp_list[2])), \
             "ед": list(set(tmp_list[3]))}

for key, val in analytics.items():
    print("%12s: " % key, end="")
    print(val)
