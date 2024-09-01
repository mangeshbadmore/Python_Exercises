
sentence = "This is common interview question"
# sentence = "ABA A BC "

dic_1 = {}
for char in sentence:
    if char in dic_1:
        print("Char present in dictionary.. Increment count")
        # old_count = dic_1[char]
        # new_count = old_count + 1
        # dic_1[char] = new_count
        dic_1[char] = dic_1[char] + 1

    else:
        dic_1[char] = 1
        print(dic_1)

print("After Loop Completion, dic_1 = ")
for key, val in dic_1.items():
    print(key, "=", val)

# Find highest repeated characters using traditional method
# max_val = 0
# counter = 0
# for key, val in dic_1.items():
#     counter += 1

#     if val > max_val:
#         max_val = val
#         max_key = key

#     if counter == dic_1.__len__():
#         print("MOST FREQUENT CHAR = ", max_key, "=", max_val)


# Find highest repeated characters using advance method
# Dictionary is key-value kind of data srtucture, without sorting capability, so we need to convert it to lists/tuples
# Send dictionary items in the form of tuples as a parameter to "sorted()"
list_of_tuples = dic_1.items()
print(list_of_tuples)

# print("Sorting Process: ")
# Now sorting function needs a key, so to pass key, which has to be number of appearances, which is second value in tuple at index '1'
# We can use lambda function, syntax : lambda input_value:return_value
# As an in put, we pass it a tuple and return value will be tuple[1] i.e. count of characters
#
sorted_list = sorted(list_of_tuples, key=lambda tuple_1: tuple_1[1])
print(sorted_list[-1])
print(* sorted_list[-1])
