"""
QUESTION:
Write a function `prevent_overflow` to prevent integer overflow when adding two integers. Assume the maximum value that can be stored is 2^31-1 and the minimum value is -2^31. The function should return the sum if it is within the valid range; otherwise, return the maximum or minimum value depending on whether the sum overflows or underflows, respectively.
"""

def prevent_overflow(a: int, b: int) -> int:
    """
    Prevent integer overflow when adding two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b if it is within the valid range; otherwise, the maximum or minimum value depending on whether the sum overflows or underflows.
    """
    max_val = 2**31 - 1
    min_val = -2**31

    sum_val = a + b

    if sum_val > max_val:
        return max_val
    elif sum_val < min_val:
        return min_val
    else:
        return sum_val