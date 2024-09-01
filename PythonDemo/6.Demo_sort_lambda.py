l = [

    ("item1", 110),
    ("item2", 90),
    ("item3", 50)

]


# def sort_f(list_item):
#     return list_item[1]


# l.sort(key=sort_f)
# Sort without defining and calling a function. Use lambda (anonymous) function and pass a parameter under expression
l.sort(key=lambda l: l[1])
print(l)


# lambda function takes inputs and return the value using SINGLE expression only
# Syntax = lambda input1, input2,...  : expression
# e.g. addition of two numbers.
##      lambda x,y : x + y
# See https://www.youtube.com/watch?v=EFjf3cx1N7o for reference
