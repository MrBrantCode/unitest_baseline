"""
QUESTION:
Write a function `quickSelect` that calculates the median of an unsorted array. The function should take the array as input and return the median value. The time complexity of the solution should not exceed O(n). Note that if the length of the array is even, the median is the average of the two middle elements.
"""

def quickSelect(nums, k):
    """
    The QuickSelect algorithm.

    Args:
    nums (list): The input list.
    k (int): The index of the desired element.

    Returns:
    int: The k-th smallest element in the list.
    """

    if len(nums) == 1:
        return nums[0]

    pivot_index = len(nums) // 2
    pivot = nums[pivot_index]

    # Partition the list into three parts
    left = [x for i, x in enumerate(nums) if x < pivot and i != pivot_index]
    middle = [x for x in nums if x == pivot]
    right = [x for i, x in enumerate(nums) if x > pivot and i != pivot_index]

    if k < len(left):
        return quickSelect(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return quickSelect(right, k - len(left) - len(middle))

def median(nums):
    """
    Calculate the median of a list.

    Args:
    nums (list): The input list.

    Returns:
    float: The median of the list.
    """

    n = len(nums)
    if n % 2 == 1:
        return quickSelect(nums, n // 2)
    else:
        return 0.5 * (quickSelect(nums, n // 2 - 1) + quickSelect(nums, n // 2))