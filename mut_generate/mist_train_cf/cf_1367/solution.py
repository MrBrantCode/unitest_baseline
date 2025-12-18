"""
QUESTION:
Implement a function called `range_check` that takes in three parameters: `number`, `lower_bound`, and `upper_bound`. The function should return `True` if `number` is within the range defined by `lower_bound` and `upper_bound` (inclusive), and `False` otherwise. The function must use a recursive binary search algorithm and not use any built-in search or sort functions, with a time complexity of O(log n), where n is the difference between `upper_bound` and `lower_bound`.
"""

def range_check(number, lower_bound, upper_bound):
    if lower_bound > upper_bound:
        return False
    mid = (lower_bound + upper_bound) // 2
    if number == mid:
        return True
    elif number < mid:
        return range_check(number, lower_bound, mid - 1)
    else:
        return range_check(number, mid + 1, upper_bound)