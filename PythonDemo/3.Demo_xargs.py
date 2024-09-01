# Magic number using single "*"
# When sent a list of numbers, such numbers can be stored by prefixing argument with "*" in function
# and it creates a TUPLE to store them

def addition(*numbers):
    total = 0
    for n in numbers:
        total += n

    return total


print("Program started")
print(addition(5, 4, 10))

print(addition(10, 20))


print("Program finished")
