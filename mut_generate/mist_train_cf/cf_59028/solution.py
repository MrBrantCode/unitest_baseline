"""
QUESTION:
Write a function called `sum_list` that takes a list as input. The list can be nested and of variable length, containing integers and non-integer types. The function should recursively iterate over the list and all its nested lists, filter out non-integer types, and sum up all integers greater than 5. The function should return the total sum.
"""

def sum_list(lst):
    total = 0
    for element in lst:
        if type(element) is list:
            total += sum_list(element)
        elif isinstance(element, int) and element > 5:
            total += element
    return total