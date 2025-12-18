"""
QUESTION:
Create a function `remove_odd_elements` that takes a nested, heterogeneous tuple `t` as input and returns a new tuple with all non-even elements removed. The function should handle various data types, including integers, floating-point numbers, strings, lists, dictionaries, complex numbers, and boolean values.

The function should recursively handle nested tuples and convert lists and dictionaries to tuples before processing. It should interpret boolean values as integers (True as 1 and False as 0) and discard them if they are not even. Strings should be retained only if they are numeric and even. Complex numbers and non-even elements should be removed from the output tuple.
"""

def remove_odd_elements(t):
    result = ()
    for i in t:
        if type(i) is bool:
            if i % 2 == 0:
                result += (i,)
        elif type(i) is tuple:
            result += (remove_odd_elements(i),)
        elif type(i) is int or type(i) is float:
            if i % 2 == 0:
                result += (i,)
        elif type(i) is complex:
            continue
        elif type(i) is str:
            if i.isnumeric() and int(i) % 2 == 0:
                result += (i,)
        elif type(i) is list or type(i) is dict:
            result += (remove_odd_elements(tuple(i)),)
    return result