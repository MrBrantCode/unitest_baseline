"""
QUESTION:
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:


Input: [10,2]
Output: "210"

Example 2:


Input: [3,30,34,5,9]
Output: "9534330"


Note: The result may be very large, so you need to return a string instead of an integer.
"""

def form_largest_number(nums):
    # Convert all numbers to strings
    nums = [str(n) for n in nums]
    
    # Sort the numbers in descending order
    nums.sort(reverse=True)
    
    # Custom sorting to ensure the largest number formation
    for i in range(1, len(nums)):
        if len(nums[i - 1]) > len(nums[i]):
            ran = len(nums[i])
            j = i
            while j - 1 >= 0 and nums[j - 1][:ran] == nums[j] and (nums[j - 1] + nums[j] <= nums[j] + nums[j - 1]):
                (nums[j - 1], nums[j]) = (nums[j], nums[j - 1])
                j -= 1
    
    # Join the sorted numbers and convert to string
    return str(int(''.join(nums)))