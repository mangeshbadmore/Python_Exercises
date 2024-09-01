l1 = [1, 2, 3, 4, 5]
s1 = set(l1)
s2 = {5, 6, 7, 8}
print(s1)
print(s2)
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 - s1)

if 3 in s1:
    print("number present in s1")
