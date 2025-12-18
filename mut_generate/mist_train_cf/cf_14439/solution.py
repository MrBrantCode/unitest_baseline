"""
QUESTION:
Implement a function `twoSum` that takes a list of integers `nums` and an integer `target` as input and returns the indices of the two numbers in `nums` that add up to `target`. Assume that each input has exactly one solution and that you may not use the same element twice.
"""

def twoSum(nums, target):
    """
    Returns the indices of the two numbers in `nums` that add up to `target`.
    
    Args:
        nums (list): A list of integers.
        target (int): The target sum.
    
    Returns:
        list: A list of two indices corresponding to the numbers in `nums` that add up to `target`.
    """
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i