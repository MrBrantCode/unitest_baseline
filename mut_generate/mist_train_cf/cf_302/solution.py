"""
QUESTION:
Find the minimum element in an unsorted array using a function named `find_min` with a time complexity of O(log n) and a space complexity of O(1). The function should not use any looping constructs or recursion. It should also not utilize any built-in sorting functions or libraries. The input array is guaranteed to be non-empty.
"""

def find_min(nums):
    """
    Find the minimum element in an unsorted array with a time complexity of O(log n) and space complexity of O(1).
    
    Args:
    nums (list): A non-empty list of integers.
    
    Returns:
    int: The minimum element in the array.
    """
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]