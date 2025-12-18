"""
QUESTION:
Write a function maxSubarrayProduct that takes an array of integers as input and returns the maximum product of the maximum and minimum numbers in each non-empty sub-array.
"""

def maxSubarrayProduct(nums):
    """
    This function calculates the maximum product of the maximum and minimum numbers 
    in each non-empty sub-array.

    Args:
        nums (list): A list of integers.

    Returns:
        int: The maximum product amongst all sub-arrays.
    """
    if not nums:
        return 0
    
    max_product = [0] * len(nums)
    min_product = [0] * len(nums)
    max_product[0] = min_product[0] = result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product[i] = max(nums[i], min_product[i-1] * nums[i])
            min_product[i] = min(nums[i], max_product[i-1] * nums[i])
        else:
            max_product[i] = max(nums[i], max_product[i-1] * nums[i])
            min_product[i] = min(nums[i], min_product[i-1] * nums[i])
        
        result = max(result, max_product[i])
    
    return result