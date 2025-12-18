"""
QUESTION:
Write a function called `replace_empty_tuples` that takes a list of tuples and a default value as input. The function should replace empty tuples in the list with the default value only if the empty tuple is preceded by a tuple of length 3. The function should return the modified list. The list can contain tuples of arbitrary length and any type of Python variable. The default value should be a tuple.
"""

def replace_empty_tuples(lst, default_value=('default_value',)):
    output = []
    for i in range(len(lst)):
        if len(lst[i]) == 0 and i > 0 and len(lst[i-1]) == 3:
            output.append(default_value)
        else:
            output.append(lst[i])
    return output