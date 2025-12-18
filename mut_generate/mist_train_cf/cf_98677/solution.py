"""
QUESTION:
Write a recursive function `sqrt_sum` that takes three arguments - `start`, `end`, and `acc` (with a default value of 10) - to calculate the square root of the sum of integers from `start` to `end` (inclusive) with an accuracy of at least `acc` decimal places.
"""

def sqrt_sum(start, end, acc=10):
    if start == end:
        return round(start**0.5, acc)
    else:
        mid = (start + end) // 2
        left_sum = sum(range(start, mid+1))
        right_sum = sum(range(mid+1, end+1))
        return round((left_sum + right_sum)**0.5, acc)