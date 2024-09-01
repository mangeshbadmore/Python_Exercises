# In range function the last item is excluded e.g. in range of 1-10, number 10 will be excluded

# List of mixed data tyoes
# a = ["a", 2, 3]
# print(a)

# Create array of same items multiple times
# b = [1] * 10
# print(b)


# Add to lists
# a = ["a", 3, 5, "Mangesh"]
# b = ["Shruthi", "Turiya", 4, 6]
# print(a + b)

# Convert range to list
# num = list(range(1, 10, 2))
# print(num)


# String to list
# chars = list("Hello")
# print(chars)


# Sort list in reverse order
# l = list(range(10))
# print(l)
# print(l[4:10:2])  # print alternate numbers, skip step with 2
# print(l[::-1])   # print reverse numbers, using -1


# Unpacking list
# z = [1, 2, "Mangesh"]
# p, q, r = z
# print(p)
# print(q)
# print(r)

# Get index of item in the list using enumerate built-in function
# In fact enumerate converts the list in tuples (index, n'th_in_list)
# iterable_list = ["A", "B", "C"]
# for n in enumerate(iterable_list):
#     print(n)
#     print(n[0], n[1])

# Since above enumeration returning a tuple, it can be accessed as below
# iterable_list = ["A", "B", "C", "D"]
# for n1, n2 in enumerate(iterable_list):
#     print(n1, n2)


# # List functions test
# ll = [13, 62, 33, 4, 572, 1]
# print(ll)
# ll.pop(3)  # remove single item
# print(ll)
# del ll[0: 2]  # delete range of items.
# print(ll)
# ll.remove(4)  # removes particular item from the list
# print(ll)


# Sort list
from operator import truediv


# o = [1, 45, 123, 7, 22]
# o.sort()                # Sorts original list, default in ASC
# print(o)
# o.sort(reverse=True)    # Sorts original list, in reverse order
# print(o)

# print(sorted(o))  # sorted() built in funion does not modify existing list
# print(sorted(o, reverse=True))  # reverse order
# print(o)          # original list remains unchanged after sorted() function

l3 = [10, 30, 40, 100, 30]
l3.append(20)
print(l3)
print(l3.count(30))
print(l3.index(20))
l3.insert(1, 400)
print(l3)
