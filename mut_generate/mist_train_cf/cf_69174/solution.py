"""
QUESTION:
Write a function `unravel(number_list)` that takes a nested list of integers as input and returns a new list containing all the integers from the input list in the same order, but without any nesting. The input list can contain any level of nested lists.
"""

def unravel(number_list, result=None):
    if result is None:
        result = []
    
    for number in number_list:
        if isinstance(number, list):
            unravel(number, result)
        else:
            result.append(number)
    
    return result