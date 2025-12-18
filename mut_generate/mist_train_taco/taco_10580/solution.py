"""
QUESTION:
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:


Input: [2,2,3,2]
Output: 3


Example 2:


Input: [0,1,0,1,0,1,99]
Output: 99
"""

def find_single_number(nums: list[int]) -> int:
    unique_elements = set(nums)
    sum_unique_elements = sum(unique_elements)
    sum_nums = sum(nums)
    result = (sum_unique_elements * 3 - sum_nums) // 2
    return result