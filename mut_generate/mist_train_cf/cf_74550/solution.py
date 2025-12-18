"""
QUESTION:
Design a function named `traverse_and_multiply` that takes an iterable and an optional initial value as arguments. The function should recursively traverse the iterable, which can be a dictionary, list, tuple, or set, and multiply all numeric values (integers and floats) together, ignoring non-numeric elements. The function should be able to handle nested data structures and return the product of all numeric values. Note that the function should be optimized for large data sets but may not be suitable for very deeply nested structures due to Python's recursion limit.
"""

def traverse_and_multiply(iterable, value=1):
    """ 
    Multiplies all numerical values within a given 
    iterable (lists, dictionaries, tuples, etc.). 
    """
    if isinstance(iterable, dict):
        for k, v in iterable.items():
            value = traverse_and_multiply(v, value)
    elif isinstance(iterable, list) or isinstance(iterable, tuple) or isinstance(iterable, set):
        for elem in iterable:
            value = traverse_and_multiply(elem, value)
    elif isinstance(iterable, int) or isinstance(iterable, float):
        value *= iterable

    return value