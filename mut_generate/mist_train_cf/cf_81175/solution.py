"""
QUESTION:
Design a function named `sum_within_bounds` that takes a list of integers `l`, an integer `lower_bound`, and an integer `upper_bound` as input. The function should return `True` if the sum of all elements in the list and the sum of the first half of the elements are both within the range defined by `lower_bound` and `upper_bound` (inclusive), and `False` otherwise. If the length of the list is not even, the function should return an error message instead.
"""

def sum_within_bounds(l: list, lower_bound: int, upper_bound: int):
    # Check if the list length is even
    if len(l) % 2 != 0:
        return "Error: List length is not even"

    # Calculate the sum of all elements and check if it's within the bounds
    total_sum = sum(l)
    if total_sum < lower_bound or total_sum > upper_bound:
        return False

    # Calculate the sum of half of the elements and check if it's within the bounds
    half_sum = sum(l[:len(l) // 2])
    if half_sum < lower_bound or half_sum > upper_bound:
        return False

    # If all checks passed, return True
    return True