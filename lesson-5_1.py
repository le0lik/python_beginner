from os import linesep
filename = "lesson-5_1.txt"

try:
    txtfile = open(filename, "w")
except IOError:
    print(f"Не удалось открыть на запись файл {filename}")

print(f"Введите строки дл язаписи в файл {filename}. Конец ввода - пустая строка")
while True:
    input_srt = input()
    if input_srt == "":
        break

    txtfile.write(input_srt + linesep)

txtfile.close()
