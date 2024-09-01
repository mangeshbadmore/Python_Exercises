# Above can be achieved with list comprehension/map as per demo
from sys import getsizeof
list_2 = [v*2+1 for v in range(10)]
print(list_2)

# If we change above to angular braces, it returns generator object, which is also an iterabe object
gen_1 = (v*2+1 for v in range(10))
for g in gen_1:
    print(g)

# Generator object are not storing values of each item and grow in it's size and that is beauty
# Lets check the size of List Vs size of generator object (iterable)

print("List Object Size = ", getsizeof(list_2))
print("Generator Object Size = ", getsizeof(gen_1))

# The size of generator object remains same because it is not storing value and growing.
# It is like temporary bucket to store value then new value comes and sit in it
# Whereas, in lists, the data in bucket gets piled up, and hence the size of object keeps growing.
