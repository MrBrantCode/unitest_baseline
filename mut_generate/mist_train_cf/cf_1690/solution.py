"""
QUESTION:
Create a function `find_max` that takes a list of integers as input. The function should return two values: the maximum value and the second maximum value in the list. If a negative number is found, it should be treated as its positive counterpart (i.e., subtract it from zero). Zero values should be ignored when finding the maximum and second maximum.
"""

def find_max(x):
    max_val = float('-inf')
    second_max_val = float('-inf')
    for i in x:
        i = abs(i) if i < 0 else i  # handle negative numbers by taking their absolute value
        if i > 0:  # ignore zero values
            if i > max_val:
                second_max_val = max_val
                max_val = i
            elif i > second_max_val and i != max_val:
                second_max_val = i
    return max_val, second_max_val