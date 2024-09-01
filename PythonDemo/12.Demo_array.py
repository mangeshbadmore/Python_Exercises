from array import array

# Search for typecode https://docs.python.org/3/library/array.html
a = array("i", [1, 2, 3, 4])
print(a)

a.extend([10, 11])
print(a)
