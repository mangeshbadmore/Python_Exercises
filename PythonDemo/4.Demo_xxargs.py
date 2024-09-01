# Magic number using double "**"
# When sent a list of numbers, such numbers can be stored by prefixing argument with "**" in function
# and it creates a DICTIONARY object to store them

def xxargs_demo_function(**numbers):
    print(numbers)
    print(numbers["country"])
    print(numbers["age"])


xxargs_demo_function(name="Mangesh", age=33, country="India")
