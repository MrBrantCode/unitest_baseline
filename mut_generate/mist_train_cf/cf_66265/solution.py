"""
QUESTION:
Create a function named `swap_first_and_last` that takes a list as an argument and returns the list with its first and last elements swapped, while maintaining the order of the remaining elements. If the list has one or zero elements, return it unchanged.
"""

def entrance(my_list):
    if len(my_list) > 1:
        my_list[0], my_list[-1] = my_list[-1], my_list[0]
    return my_list