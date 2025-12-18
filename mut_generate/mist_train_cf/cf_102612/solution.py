"""
QUESTION:
Implement a function called `sortDescending` that takes a list of integers as input and sorts it in descending order. The function should use O(1) extra space and have a time complexity of O(n log n), where n is the length of the list. The input list may contain duplicates and have a length of up to 10^6.
"""

def sortDescending(nums):
    """
    Sorts the input list of integers in descending order.

    Args:
    nums (list): A list of integers.

    Returns:
    list: The sorted list in descending order.
    """
    nums.sort(reverse=True)
    return nums