"""
QUESTION:
Construct a function named `sum_within_bounds` that takes a list of integers `l` and two integers `lower_bound` and `upper_bound` as parameters. The function should return `True` if the length of `l` is even, the sum of all elements in `l` is within the range `[lower_bound, upper_bound]`, and the sum of the first half of the elements in `l` is within the same range; otherwise, it should return `False`.
"""

def sum_within_bounds(lst, lower_bound, upper_bound):
    if len(lst) % 2 != 0:
        return False
    total_sum = sum(lst)
    half_sum = sum(lst[i] for i in range(len(lst) // 2))
    return lower_bound <= total_sum <= upper_bound and lower_bound <= half_sum <= upper_bound