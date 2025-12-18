"""
QUESTION:
Design a function named `find_second_maximum` that takes a list of numbers as input and returns the second maximum value from the list. The function should handle edge cases where the list is empty or has less than 2 unique elements, and it should correctly handle lists containing negative numbers and duplicates. The function should return `None` if no second maximum value exists.
"""

def find_second_maximum(lst):
    if len(lst) < 2:
        return None
    max_val = second_max = float('-inf')
    unique_elements = set(lst)
    if len(unique_elements) < 2:
        return None
    for num in unique_elements:
        if num > max_val:
            second_max = max_val
            max_val = num
        elif num > second_max:
            second_max = num
    return second_max