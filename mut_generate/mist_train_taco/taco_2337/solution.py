"""
QUESTION:
Given an array of integers, return the smallest common factors of all integers in the array.

When i say **Smallest Common Factor** i mean the smallest number above 1 that can divide all numbers in the array without a remainder.

If there are no common factors above 1, return 1 (technically 1 is always a common factor).
"""

def smallest_common_factor(lst):
    """
    Find the smallest common factor of all integers in the given list.

    Parameters:
    lst (list of int): The list of integers to find the smallest common factor for.

    Returns:
    int: The smallest common factor of all integers in the list. If no common factor above 1 exists, returns 1.
    """
    return next((k for k in range(2, 1 + min(lst, default=1)) if all((n % k == 0 for n in lst))), 1)