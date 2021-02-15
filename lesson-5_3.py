filename = "lesson-5_3.txt"
with open(filename) as txtfile:
    count_people = 0
    total_summ = 0
    for line in txtfile:
        name, text_val = line.split(" ")
        val = int(text_val)
        count_people += 1
        total_summ += val
        if val < 20000:
            print(f"{name} имеет зарплату менее 20000")
    print(f"Средняя зарплата: {total_summ / count_people}")
