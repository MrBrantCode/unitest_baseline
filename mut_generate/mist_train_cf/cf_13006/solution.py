"""
QUESTION:
Implement a function `shift_elements` that takes a list and shifts each element two positions to the right, wrapping around to the start of the list when necessary.
"""

def shift_elements(a):
    """
    Shifts each element in the list two positions to the right, wrapping around to the start of the list when necessary.

    Args:
        a (list): The input list.

    Returns:
        list: The modified list with elements shifted two positions to the right.
    """
    n = len(a)
    a[:] = a[-2:] + a[:-2]
    return a