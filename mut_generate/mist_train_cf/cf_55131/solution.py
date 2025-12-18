"""
QUESTION:
Write a function named `sum_within_bounds` that takes a list of integers `l`, a lower bound `lower_bound`, and an upper bound `upper_bound` as input. The function should return `True` if the length of the list is even and the sum of all elements in the list is within the range `[lower_bound, upper_bound]` (inclusive), and `False` otherwise.
"""

def sum_within_bounds(l: list, lower_bound: int, upper_bound: int):
    if len(l) % 2 == 0:
        s = sum(l)
        if lower_bound <= s <= upper_bound:
            return True
        else:
            return False
    else:
        return False