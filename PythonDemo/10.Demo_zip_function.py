from hashlib import new


# ZIP function combines items from diff list at matching index and form a tuple


list1 = [10, 20, 30]
list2 = [1000, 2000, 3000]
if type(list1) is list:
    print("It is list")
new_tuple = list(zip(list1, list2))
print(new_tuple)

# Zip string which is also iterable input
print(list(zip(list1, list2, "ABCD")))
