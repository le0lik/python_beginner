filename = "lesson-5_2.txt"
with open(filename) as txtfile:
    n = 0
    for line in txtfile:
        n += 1
        print(f'Слов в строке строке {n}: {len(line.split(" "))}')

    print(f"Всего {n} строк")
