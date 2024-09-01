# Print odd numbers
# list_1 = []
# for v in range(5):
#     list_1.append(v*2+1)

# print(list_1)

# Above can be achieved with list comprehension/map as per demo
list_2 = [v*2+1 for v in range(5)]
print(list_2)

# Similarly, we can write code for dictionary comprehension
dic_1 = {v: v*2+1 for v in range(5)}
print(dic_1)

# From list_2 object, if we replace square braces with curly braces, it becomes set
set_1 = {v*2+1 for v in range(5)}
print(set_1)

# If we change above to angular braces, it returns generator object
gen_1 = (v*2+1 for v in range(5))
print(gen_1)

# Generator object are not storing values of each item and grow in it's size and that is beauty
