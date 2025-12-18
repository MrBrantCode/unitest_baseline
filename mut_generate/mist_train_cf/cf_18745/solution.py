"""
QUESTION:
Delete all occurrences of a specified value from a given list and return the resulting list in ascending order. The function name is not specified. 

The function should take a list of integers and an integer value as input, remove all occurrences of the specified value from the list, and return the resulting list in ascending order.
"""

def delete_value(lst, val):
    return sorted([x for x in lst if x != val])