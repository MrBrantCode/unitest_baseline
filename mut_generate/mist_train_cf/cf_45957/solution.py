"""
QUESTION:
Write a function `multiply_distinct_numbers` that takes an array as input and returns the product of its distinct numerical elements (integers and floats). The function should ignore non-numerical elements and duplicates, and it should work for arrays containing a mix of data types.
"""

def multiply_distinct_numbers(array):
    distinct_values = set([val for val in array if isinstance(val, (int, float))])
    product = 1
    for value in distinct_values:
        product *= value
    return product