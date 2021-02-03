num = int(input("Введите целое положительное число: "))
n_max = 0
while num > 0:
    n = num % 10
    num //= 10

    if n > n_max:
        n_max = n

    #print(f"{num} : {n} : {n_max}")

print(f"Наибольшая цифра в числе равна {n_max}")