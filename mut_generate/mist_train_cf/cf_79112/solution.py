"""
QUESTION:
Create a function `sum_multidimensional_list` that calculates the sum of numbers within a multidimensional list in Python. The function should not use the built-in `sum` function and should ignore non-numeric values. The function should work with lists of arbitrary depth and should handle both integers and floats.
"""

def sum_multidimensional_list(lst):
    total = 0
    for i in lst:
        if type(i) == list:
            total += sum_multidimensional_list(i)
        elif isinstance(i, (int, float)):
            total += i
    return total