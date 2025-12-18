"""
QUESTION:
Write a function `sum_nested` that takes a nested list as input and returns the sum of all integers in the list, including integers in any sublists. The function should handle nested lists of arbitrary depth.
"""

def sum_nested(nested_list):
    total = 0
    for element in nested_list:
        if type(element) is list:  
            total += sum_nested(element)  
        else:  
            total += element  
    return total