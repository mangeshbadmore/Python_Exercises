
# Craete tuple without parenthesis
t2 = 1, 2, 3  # Letters cannot be assignged
print(type(t2))
print(t2)

# Convert list to tuple
list1 = ["amar", "mangesh", "nandan"]
print(list1)
t3 = tuple(list1)
print(type(t3))

# Convert list of letters to tuple
print(tuple("HellO"))

# Tuple of repeated values
t4 = ("ACDC") * 3
print(t4)

# Check existence of a letter in tuple
if "Z" in t4:
    print("Letter exists!")
