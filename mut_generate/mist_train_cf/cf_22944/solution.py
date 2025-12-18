"""
QUESTION:
Write a function `max_pair_sum` that takes an array of integers as input and returns the maximum sum of two pairs of distinct positive integers in the array. The integers in each pair should add up to a sum less than or equal to 100. The array can contain both positive and negative integers, and the integers in each pair should be distinct.
"""

def max_pair_sum(nums):
    """
    This function takes an array of integers as input and returns the maximum sum of two pairs of distinct positive integers in the array.
    
    The integers in each pair should add up to a sum less than or equal to 100.
    
    Parameters:
    nums (list): A list of integers.
    
    Returns:
    int: The maximum sum of two pairs of distinct positive integers in the array.
    """
    
    # Filter out non-positive integers and sort the array in descending order
    nums = sorted([num for num in nums if num > 0], reverse=True)
    
    # Initialize variables to store the maximum pair sum
    max_sum = 0
    
    # Iterate over the sorted array to find the maximum pair sum
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] <= 100:
                max_sum = max(max_sum, nums[i] + nums[j])
    
    return max_sum