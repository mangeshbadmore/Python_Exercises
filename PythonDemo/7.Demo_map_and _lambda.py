# lambda function takes inputs and return the value using SINGLE expression only
# Syntax = lambda input1, input2,...  : expression
# e.g. addition of two numbers.
##      lambda x,y : x + y
# See https://www.youtube.com/watch?v=EFjf3cx1N7o for reference

items_list = [

    ("item1", 110),
    ("item2", 90),
    ("item3", 50)

]

map_val = map(lambda parm: parm[1], items_list)
for i in map_val:
    print(i)


def reminder(x): return x % 3


print(reminder(3))
