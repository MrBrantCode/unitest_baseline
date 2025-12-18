"""
QUESTION:
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:


Input: [1,2,0]
Output: 3


Example 2:


Input: [3,4,-1,1]
Output: 2


Example 3:


Input: [7,8,9,11,12]
Output: 1


Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""

def find_first_missing_positive(nums):
    nums = sorted(set(nums), key=lambda x: x)
    result = 0
    for i in range(len(nums)):
        if nums[i] <= 0:
            continue
        elif nums[i] == result + 1:
            result += 1
        else:
            break
    return result + 1