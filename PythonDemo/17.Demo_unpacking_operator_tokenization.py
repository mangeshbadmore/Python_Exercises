# When unpacked, individual items will be displayed separately

# Unpack a list
list_1 = [10, 25, 23, 324]
print(*list_1)

# Unpack a string
string_1 = "PYTHON"
print(*string_1)
print(*"JAVA")

# Unpack a range, little different. Range --> List --> Unpack
list_2 = [*range(1, 10)]
print(*list_2)

# Unpack multiple lists together mode
print(*list_1, *list_2)

# Unpack a dictionary, may be not so useful. Demo was
dic_1 = {"key1": "val1", "key2": "val2"}
dic_2 = {"key3": "val3", "key4": "val4", "key5": "val5"}
list_3 = {**dic_1}
print(list_3)

# Combine dictionary
list_4 = {**dic_1, **dic_2}
print(list_4)
