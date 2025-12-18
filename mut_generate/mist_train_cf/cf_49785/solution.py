"""
QUESTION:
Write a function `is_integer_in_range` that takes two arguments: an input `n` and a range `r` specified as a tuple of two integers. The function should return `True` if `n` is an integer within the range `r`, and `False` otherwise. The function should be able to handle large integer inputs efficiently.
"""

def is_integer_in_range(n, r):
    # Check if input is an integer
    if isinstance(n, int):
        # Check if integer is in the specified range
        if r[0] <= n <= r[1]:
            return True
    return False