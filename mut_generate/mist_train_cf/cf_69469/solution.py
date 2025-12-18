"""
QUESTION:
Write a function max_subarray_sum that takes a list of integers as input and returns the maximum subarray sum with a minimum subarray length of 2. If the input list has less than 2 elements, return None.
"""

def max_subarray_sum(nums):
    # check if there are at least 2 numbers in the list
    if len(nums) < 2:
        return None
    
    # Initialize current sum and max sum as the sum of first two elements
    curr_sum = max_sum = nums[0] + nums[1]
    
    # Iterate over the list from the 3rd element
    for num in nums[2:]:
        # If the current number is greater than the current sum plus the current number
        # that means the current sum is negative, so update the current sum as the current number
        curr_sum = max(num, curr_sum + num)
        
        # After updating the current sum, check with the max sum,
        # If the current sum is more than the max sum, update the max sum as the current sum.
        max_sum = max(curr_sum, max_sum)
    
    return max_sum