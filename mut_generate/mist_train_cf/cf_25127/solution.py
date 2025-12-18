"""
QUESTION:
Write a method named `findDuplicate` that takes an array of integers as input and returns a boolean indicating whether the array contains any duplicate elements. The method should traverse the array only once and use constant space complexity is not required but efficiency is preferred.
"""

def findDuplicate(arr):
    """
    This function checks if an array contains any duplicate elements.

    Args:
        arr (list): A list of integers.

    Returns:
        bool: True if the array contains duplicate elements, False otherwise.
    """
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False