test_list = [1, "test", 3.14, 'text', 2+1j, [1, 2], (4, 5), {1:"x", 2:"y"}]
for val in test_list:
    print(f"{val}: {type(val)}")
