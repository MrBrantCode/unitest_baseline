"""
QUESTION:
Find the median element in a list of n elements (1 ≤ n ≤ 10^6). The solution should have a time complexity of O(n log n). Implement the function `find_median` that takes a list of integers as input and returns the median element.
"""

def find_median(nums):
    """
    Find the median element in a list of integers.

    Args:
        nums (list): A list of integers.

    Returns:
        float: The median element in the list.
    """
    nums.sort()
    n = len(nums)
    
    # If n is odd, the median element is the middle element
    if n % 2 != 0:
        return nums[n // 2]
    # If n is even, the median element is the average of the two middle elements
    else:
        mid1 = nums[n // 2 - 1]
        mid2 = nums[n // 2]
        return (mid1 + mid2) / 2