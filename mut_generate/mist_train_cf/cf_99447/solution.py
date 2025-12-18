"""
QUESTION:
Create a function `concatenate_digits(num)` that takes a non-negative integer `num` (0 <= num <= 10^9) and returns a string of concatenated digits. Include error handling to return "Invalid input" if `num` is not a valid integer within the specified range.
"""

def concatenate_digits(num):
    """
    Concatenates the digits of a non-negative integer.

    Args:
        num (int): A non-negative integer.

    Returns:
        str: A string of concatenated digits if num is valid, "Invalid input" otherwise.
    """
    if not isinstance(num, int) or num < 0 or num > 10**9:
        return "Invalid input"
    else:
        return ''.join(str(digit) for digit in str(num))