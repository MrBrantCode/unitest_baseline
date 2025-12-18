"""
QUESTION:
Create a function `sum_nested` that calculates the cumulative total of all numeric elements within a list and its sub-lists, ignoring non-numeric values. The function should handle lists containing integers, floats, and nested lists with integers or floats.
"""

def sum_nested(lst):
    total = 0
    
    for element in lst:
        if type(element) == list:
            total += sum_nested(element)
        elif type(element) in (int, float):
            total += element
            
    return total