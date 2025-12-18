"""
QUESTION:
Create a function named `reverse_copy` that takes a list `original_list` as input and returns a new list that is a reversed copy of `original_list`. The function should not use any built-in list methods or functions for reversing or copying.
"""

def reverse_copy(original_list):
    reversed_list = []
    for i in range(len(original_list)-1, -1, -1):
        reversed_list.append(original_list[i])
    return reversed_list