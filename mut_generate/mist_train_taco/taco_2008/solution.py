"""
QUESTION:
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:


Input: [3,2,3]
Output: 3

Example 2:


Input: [2,2,1,1,1,2,2]
Output: 2
"""

def find_majority_element(nums):
    n = len(nums)
    if n == 1:
        return nums[0]
    if n % 2:
        find = set(nums[0:n // 2 + 1]) & set(nums[n // 2:])
    else:
        find = set(nums[0:n // 2]) & set(nums[n // 2:])
    for i in find:
        if nums.count(i) > n // 2:
            return i