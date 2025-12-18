"""
QUESTION:
Write a function `find_min` that takes an unsorted array of integers as input and returns the minimum value in the array. The function should have a time complexity of O(log n) or better. The input array is guaranteed to be non-empty.
"""

def find_min(nums):
    """
    Find the minimum value in an unsorted array of integers.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The minimum value in the array.

    Time Complexity: O(n) as we are scanning the array only once.
    """
    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val