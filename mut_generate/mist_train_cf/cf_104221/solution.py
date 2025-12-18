"""
QUESTION:
Write a function `twoSum` that takes an array of integers and a target integer as input, and returns the indices of the two numbers in the array that add up to the target, where the first index is less than the second. The function must remove any duplicate elements from the array in linear time complexity (O(n)). The array may contain duplicate integers.
"""

def twoSum(nums, target):
    """
    Returns the indices of the two numbers in the array that add up to the target.
    
    Args:
        nums (list): A list of integers.
        target (int): The target integer.
    
    Returns:
        list: A list containing the indices of the two numbers.
    """
    seen = {}
    unique_nums = []
    for i, num in enumerate(nums):
        if num not in seen:
            unique_nums.append(num)
            seen[num] = i
        if target - num in seen and seen[target - num] != i:
            return [seen[target - num], seen[num]]
    return None