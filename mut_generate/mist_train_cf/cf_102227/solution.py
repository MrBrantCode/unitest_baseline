"""
QUESTION:
Create a function `remove_sort_list(lst)` that takes a list of integers as input. The function should remove the second to last element from the list and sort the remaining elements in ascending order. If the input list has less than 2 elements, return the original list.
"""

def remove_sort_list(lst):
    if len(lst) < 2:
        return lst

    lst.pop(-2)  # Remove second to last element
    lst.sort()   # Sort the list in ascending order

    return lst