"""
QUESTION:
Return the Nth Even Number

The input will not be 0.
"""

def get_nth_even_number(n: int) -> int:
    """
    Returns the Nth even number.

    Args:
        n (int): The position of the even number to be returned. Must be greater than 0.

    Returns:
        int: The Nth even number.
    """
    return 2 * (n - 1)