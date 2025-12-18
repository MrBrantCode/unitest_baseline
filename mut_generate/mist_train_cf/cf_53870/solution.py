"""
QUESTION:
Create a function `remove_odd_elements(t)` that takes a nested heterogeneous tuple `t` as input and returns a new tuple with all non-even elements removed. The function should handle nested tuples, integers, floating-point numbers, and strings, as well as lists and dictionaries embedded within the tuple. If a string is numeric and even, it should be retained; otherwise, it should be discarded. Lists and dictionaries should be converted to tuples before processing.
"""

def remove_odd_elements(t):
    result = ()
    for i in t:
        if isinstance(i, tuple):
            result += (remove_odd_elements(i),)
        elif isinstance(i, list) or isinstance(i, dict):
            result += (remove_odd_elements(tuple(i)),)
        elif isinstance(i, int) and i % 2 == 0:
            result += (i,)
        elif isinstance(i, float) and i.is_integer() and i % 2 == 0:
            result += (int(i),)
        elif isinstance(i, str):
            if i.isnumeric() and int(i) % 2 == 0:
                result += (i,)
    return result