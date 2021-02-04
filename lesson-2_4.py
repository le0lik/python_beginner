long_string = input("Ввредите строку из слов разделенных пробелом:")
for n, w in enumerate(long_string.split(" ")):
    print(f"{n}: {w[:10]}")
