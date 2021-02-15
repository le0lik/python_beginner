from functools import reduce

filename = "lesson-5_5.out"
number_list = [10, 2, 3, 234, 4, 2, 10, 6, 12]

with open(filename, "w+") as newfile:
    for n in number_list:
        newfile.write(str(n) + " ")

    newfile.seek(0)

    print(reduce(lambda p1, p2: int(p1) + int(p2), newfile.readline().strip().split(" ")))

