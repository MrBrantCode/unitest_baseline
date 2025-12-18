"""
QUESTION:
Write a recursive function named `sqrt_sum` that takes two integers `start` and `end` and an optional integer `acc` (default is 10) as input and returns the square root of the sum of integers from `start` to `end` (inclusive) with an accuracy of at least `acc` decimal places.
"""

def sqrt_sum(start, end, acc=10):
    if start == end:
        return round(start**0.5, acc)
    else:
        mid = (start + end) // 2
        left_sum = sum(range(start, mid+1))
        right_sum = sum(range(mid+1, end+1))
        return round((left_sum + right_sum)**0.5, acc)