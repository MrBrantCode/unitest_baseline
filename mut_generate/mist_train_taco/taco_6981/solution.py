"""
QUESTION:
Determine the total number of digits in the integer (`n>=0`) given as input to the function. For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.

All inputs will be valid.
"""

def count_digits(n: int) -> int:
    """
    Counts the total number of digits in the given non-negative integer `n`.

    Parameters:
    n (int): The non-negative integer whose digits are to be counted.

    Returns:
    int: The total number of digits in `n`.
    """
    return len(str(n))