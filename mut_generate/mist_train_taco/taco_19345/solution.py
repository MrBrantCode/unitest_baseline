"""
QUESTION:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:


Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

def max_subarray_sum(nums: list[int]) -> int:
    """
    Finds the maximum sum of a contiguous subarray within the given array.

    Parameters:
    - nums (list[int]): The input array of integers.

    Returns:
    - int: The maximum sum of a contiguous subarray.
    """
    if not nums:
        return 0
    
    max_sum = csum = nums[0]
    for num in nums[1:]:
        if num >= csum + num:
            csum = num
        else:
            csum += num
        if csum > max_sum:
            max_sum = csum
    
    return max_sum