"""
QUESTION:
Write a function `sum_nested_list` that takes a nested list as input and returns the sum of all elements within the list, including elements in sublists. The function should be able to handle lists of arbitrary depth and should not lose conciseness.
"""

def sum_nested_list(nested_list):
    total_sum = 0
    for i in nested_list:
        if isinstance(i, list):         
            total_sum += sum_nested_list(i)
        else:
            total_sum += i
    return total_sum