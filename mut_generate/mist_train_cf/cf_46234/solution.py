"""
QUESTION:
Implement a function called `max_subarray_sum` that takes an array of integers as input and returns the maximum cumulative sum of a continuous subsequence within the array. The function should handle edge cases such as an empty array, an array with all negative numbers, an array with all positive numbers, and an array with alternating positive and negative numbers.
"""

def max_subarray_sum(nums):
    """
    Returns the maximum cumulative sum of a continuous subsequence within the given array.
    
    Args:
        nums (list): An array of integers.
    
    Returns:
        int: The maximum cumulative sum of a continuous subsequence.
    """
    
    # Handle edge case: empty array
    if not nums:
        return 0
    
    # Initialize maxCurrent and maxGlobal to the first value of the array
    max_current = max_global = nums[0]
    
    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Update maxCurrent to be the maximum of the current number and the sum of the current number and maxCurrent
        max_current = max(num, num + max_current)
        
        # Update maxGlobal if maxCurrent is greater
        if max_current > max_global:
            max_global = max_current
    
    return max_global