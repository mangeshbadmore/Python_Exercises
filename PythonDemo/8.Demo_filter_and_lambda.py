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

filtered_values = filter(lambda parm: parm[1] > 60, items_list)
for i in filtered_values:
    print(i[1])
