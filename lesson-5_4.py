filename = "lesson-5_4.txt"
outfile = "lesson-5_4.out"
separator = " - "

change_dict = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре", "Five":"Пять",
               "Six":"Шесть", "Seven":"Семь", "Eight":"Восемь", "Nine":"Девять", "Zero":"Ноль"}

with open(filename) as txtfile:
    with open(outfile, "w") as newfile:
        for line in txtfile:
            line_list = line.split(separator)
            line_list[0] = change_dict[str(line_list[0]).title()]
            # print(line_list)
            newfile.write(separator.join(line_list))
