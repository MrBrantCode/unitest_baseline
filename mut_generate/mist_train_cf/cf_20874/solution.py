"""
QUESTION:
Implement a function called `swap_first_last` that takes a list of integers as input and returns a new list with the first and last elements swapped. The function must have a time complexity of O(1) and should not use any additional variables or built-in functions to store or manipulate the list. If the input list has less than 2 elements, return the original list.
"""

def swap_first_last(lst):
    if len(lst) < 2:
        return lst
    lst[0] = lst[0] ^ lst[-1]
    lst[-1] = lst[0] ^ lst[-1]
    lst[0] = lst[0] ^ lst[-1]
    return lst