"""
QUESTION:
Write a function `count_total_elements` that takes a list `input_list` as input, where some elements may be nested lists. The function should return the total number of elements in the list, including the elements within nested lists. Use a recursive approach.
"""

def count_total_elements(input_list):
    total_count = 0
    for item in input_list:
        if isinstance(item, list):
            total_count += count_total_elements(item)  # Recursively count elements in nested lists
        else:
            total_count += 1  # Increment count for non-list elements
    return total_count