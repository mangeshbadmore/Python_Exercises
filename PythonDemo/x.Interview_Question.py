def json_diff(obj1, obj2):
    """
    Input:
        two objects that are either a list or a dictionary.
        The objects contain value(s) that can be string, integer, list or dictionary.
        If the object is a dictionary, the key is any string.

    Output:
        list of results containing a tuple of (key, value1, value2) if value1 != value2, where value1 and value2 are values of obj1 and obj2 respectively.

    This is an open book problem.
    You may search for anything, other than for a solution to the problem.

    Pesudo-code is acceptable.

    You will be assessed on how you approach the problem, not on how accurate your syntax is or how many searches you do.

    For example, the following is acceptable:
        if object is dict then
            for key and value in dict object
                if value is not list or dict then
                    add to output (key, value, ...)
                else
                    ...
        return output
    """


...

# Some sample cases to consider:

# empty case
json_diff(["a"], ["a"])  # [ ]
json_diff({"a": 1}, {"a": 1})  # [ ]

# simple case
json_diff(["a"], ["b"])  # [ (???, "a", "b") ]
json_diff({"a": 1}, {})  # [ ("a", 1, None) ]
json_diff({"a": 1}, {"a": 2})  # [ ("a", 1, 2) ]


def json_diff(obj1, obj2):

