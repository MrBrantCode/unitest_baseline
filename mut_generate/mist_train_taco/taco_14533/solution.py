"""
QUESTION:
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:


Input:  [1,2,3,4]
Output: [24,12,8,6]


Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

def product_except_self(nums):
    n = len(nums)
    
    # Initialize the result array with 1s
    result = [1] * n
    
    # Calculate the prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Calculate the suffix products and multiply with the prefix products
    suffix = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result