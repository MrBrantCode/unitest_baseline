"""
QUESTION:
Write a function `reverse_list` that takes a list of integers as input and returns a new list with the same integers in reverse order. The function should not use any built-in Python functions for reversing a list, such as `list.reverse()` or slicing with a step of -1. The input list should remain unmodified.
"""

def reverse_list(input_list):
    # create an empty list to store the reversed sequence
    reversed_list = []
    # for each item in the original list
    for i in range(len(input_list)):
        # take the last element of the original list and append it to the reversed list
        reversed_list.append(input_list[len(input_list) - 1 - i])

    return reversed_list