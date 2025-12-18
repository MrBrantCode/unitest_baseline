"""
QUESTION:
Write a function `increasingTriplet(nums)` that takes an array of integers as input and returns a boolean indicating whether there exists a trio of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. The function should operate within O(n) time complexity and O(1) space complexity, where 1 <= nums.length <= 10^5 and -2^31 <= nums[i] <= 2^31 - 1.
"""

def increasingTriplet(nums):
    first = second = float('inf')
    
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    
    return False