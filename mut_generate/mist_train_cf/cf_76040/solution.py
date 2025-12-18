"""
QUESTION:
Given an array `nums` of integers, write a function `findNumbers` that returns the count of numbers in `nums` that have an even number of digits and the sum of those digits is also even. 

Constraints: `1 <= nums.length <= 500` and `1 <= nums[i] <= 10^5`.
"""

def findNumbers(nums):
    count = 0
    for num in nums:
        num_str = str(num)
        if len(num_str) % 2 == 0:
            sum_of_digits = sum(int(d) for d in num_str)
            if sum_of_digits % 2 == 0:
                count += 1
    return count