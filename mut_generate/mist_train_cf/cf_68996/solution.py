"""
QUESTION:
Write a function named `get_max_value_and_indices` that takes a list of integers as input and returns a list of tuples, where each tuple contains the maximum value in the list and its corresponding index. If the maximum value appears multiple times in the list, the function should return all indices where the maximum value is located. Do not use built-in Python functions to find the maximum value or its index.
"""

def get_max_value_and_indices(num_list):
    if len(num_list) == 0:
        return []

    max_val = num_list[0]
    max_indices = [0]

    for i in range(1, len(num_list)):
        if num_list[i] > max_val:
            max_val = num_list[i]
            max_indices = [i]  # new max found, so reset the list
        elif num_list[i] == max_val:
            max_indices.append(i)  # same max found, so append to the list

    return [(max_val, index) for index in max_indices]