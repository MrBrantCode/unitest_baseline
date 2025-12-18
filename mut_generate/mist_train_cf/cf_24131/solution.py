"""
QUESTION:
Given an array of integers and a target sum, write a function `twoSum` that returns the indices of the two numbers in the array that add up to the target. Assume that each input has exactly one solution and that each element can only be used once. The function should take an array of integers and the target sum as input and return an array of two indices.
"""

def two_sum(nums, target):
    """
    Returns the indices of the two numbers in the array that add up to the target.
    
    Args:
    nums (list): A list of integers.
    target (int): The target sum.
    
    Returns:
    list: A list of two indices.
    """
    result = [0, 0]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                result[0] = i
                result[1] = j
                break
    return result