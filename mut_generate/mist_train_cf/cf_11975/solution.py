"""
QUESTION:
Write a function `update_array` that takes an array of integers as input and updates it by replacing all the zeroes with the nearest non-zero element on the left side of the zero. If there is no non-zero element on the left side, replace the zero with -1.
"""

def update_array(nums):
    """
    Updates the input array by replacing all zeroes with the nearest non-zero element on the left side.
    If there is no non-zero element on the left side, replace the zero with -1.

    Args:
        nums (list): A list of integers.

    Returns:
        list: The updated list of integers.
    """
    if not nums:
        return nums
    
    result = [nums[0] if nums[0] != 0 else -1]
    
    for i in range(1, len(nums)):
        if nums[i] == 0:
            result.append(result[-1])
        else:
            result.append(nums[i])
    
    return result