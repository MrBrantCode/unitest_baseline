"""
QUESTION:
Write a function `square_nested_list` that takes a nested list of integers as input, squares each integer, and returns the resulting list. The function should be able to handle any depth of nesting. The input list can contain integers and nested lists of integers.
"""

def square_nested_list(lst):
    result = []
    for i in lst:
        if type(i) == list:
            result.append(square_nested_list(i))
        else:
            result.append(i**2)
    return result