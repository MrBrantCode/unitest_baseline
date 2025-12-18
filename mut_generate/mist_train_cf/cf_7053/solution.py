"""
QUESTION:
Write a function `twoSum` that takes a non-empty array of unique integers `nums` and a target integer `target` as input. Return the indices of two numbers in the array that add up to the target sum, without using the same number twice. The indices should be in ascending order and should be the smallest possible pair if there are multiple pairs that add up to the target sum. If there is no pair that adds up to the target sum, return an empty array. The function should have a time complexity of O(n), where n is the length of the array.
"""

def twoSum(nums, target):
    """
    Returns the indices of two numbers in the array that add up to the target sum.
    
    Args:
        nums (list): A non-empty array of unique integers.
        target (int): The target sum.
    
    Returns:
        list: The indices of two numbers in the array that add up to the target sum.
    """
    num_dict = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    
    return []