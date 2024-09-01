# Define scope of variable

v = 10


def scope_demo_function():
    # here using global keyword, we are REFERENCING value of global var, this can be useful in some situations.
    #global v
    v = 30  # this is local variable and it is completely diff from global var

    print(v)


scope_demo_function()
print(v)  # Calls global value
