
age = 18

# Writing in single line
print("Student eligible for loan") if age > 18 else print(
    "Student not eligible for loan")


# Chaining operator
if 0 < age < 18:
    print("Age is between 0 to 18")
else:
    print("Age is >= 18")


# For and Else combination
state = False

for n in range(1, 4):
    print("Attempt", n)
    if state:
        print("Success")
        break

else:
    print("Failed after 3-attempts")

# Formatted string and
print(f"This is big message {state}")

# Formatted multi-line string
print(""""
Hi
I am Mangesh 
        I love writing nice lines
""")
