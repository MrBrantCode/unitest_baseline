"""
QUESTION:
Create a function named `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed while maintaining the original order. The solution should have a time complexity of O(n) and should not use any built-in functions or libraries for removing duplicates.
"""

def remove_duplicates(nums):
    """
    Removes duplicate elements from a list of integers while maintaining the original order.

    Args:
    nums (list): A list of integers.

    Returns:
    list: A new list with duplicate elements removed.
    """
    seen = {}
    result = []

    for num in nums:
        if num not in seen:
            seen[num] = True
            result.append(num)

    return result