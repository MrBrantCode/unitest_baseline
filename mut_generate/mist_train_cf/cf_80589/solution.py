"""
QUESTION:
Write a function named `add_lists` that takes two lists of integers as input and returns a new list where each element at index `i` is the sum of the elements at index `i` in the input lists. If the lists are of unequal length, consider the missing elements in the shorter list as 0. Do not use any built-in Python functions or libraries for list manipulation.
"""

def add_lists(list1, list2):
    # Determine which list is longer
    max_len = len(list1) if len(list1) > len(list2) else len(list2)

    # Result list
    result = []

    # Add corresponding elements
    for i in range(max_len):
        # Handle case where indices are out of range for shorter list
        if i < len(list1) and i < len(list2):
            result.append(list1[i] + list2[i])
        elif i < len(list1):
            result.append(list1[i])
        else:
            result.append(list2[i])

    return result