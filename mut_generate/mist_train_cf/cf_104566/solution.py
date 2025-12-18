"""
QUESTION:
Write a function `closest_pair` that takes a list of distinct integers and a target integer as input, and returns a list of two distinct integers from the list that add up to the target value. The returned integers should be in ascending order. If there are multiple such pairs, return the pair with the smallest absolute difference between the two integers. If no such pair exists, return an empty list.
"""

def closest_pair(nums, target):
    """
    Returns a list of two distinct integers from the list that add up to the target value.
    The returned integers are in ascending order. If there are multiple such pairs, 
    return the pair with the smallest absolute difference between the two integers. 
    If no such pair exists, return an empty list.

    Args:
        nums (list): A list of distinct integers.
        target (int): The target integer.

    Returns:
        list: A list of two distinct integers.
    """
    nums.sort()
    left, right = 0, len(nums) - 1
    closest = float('inf')
    result = []
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            if abs(nums[right] - nums[left]) < closest:
                closest = abs(nums[right] - nums[left])
                result = [nums[left], nums[right]]
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return result