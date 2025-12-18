"""
QUESTION:
Implement the `sort_descending` function to sort a list of integers in descending order. The function must use O(1) extra space and run in O(n log n) time complexity, where n is the length of the list. The input list may contain duplicates and have a length of up to 10^6.
"""

def sort_descending(nums):
    """
    Sorts a list of integers in descending order using O(1) extra space and O(n log n) time complexity.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The sorted list in descending order.
    """
    nums.sort(reverse=True)
    return nums