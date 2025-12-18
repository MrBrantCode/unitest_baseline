"""
QUESTION:
Write a function named `sum_list_recursive` that calculates the sum of the elements in a given list using recursion. The function should take a list as an argument and return the sum. The function should handle lists of any length, including empty lists and lists with one element.
"""

def sum_list_recursive(lst):
    if len(lst) == 0:
        return 0
    elif len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_list_recursive(lst[1:])