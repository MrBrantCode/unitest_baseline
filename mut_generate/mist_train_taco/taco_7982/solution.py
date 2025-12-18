"""
QUESTION:
Given an array nums of positive integers, return the longest possible length of an array prefix of nums, such that it is possible to remove exactly one element from this prefix so that every number that has appeared in it will have the same number of occurrences.
If after removing one element there are no remaining elements, it's still considered that every appeared number has the same number of ocurrences (0).
 
Example 1:
Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4]=5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.

Example 2:
Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13

Example 3:
Input: nums = [1,1,1,2,2,2]
Output: 5

Example 4:
Input: nums = [10,2,8,9,3,8,1,5,2,3,7,6]
Output: 8

 
Constraints:

2 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""

from collections import Counter

def longest_equal_freq_prefix(nums):
    def isvalid(C):
        if len(C) > 2:
            return False
        if len(C) == 1:
            a = min(C)
            if a == 1 or C[a] == 1:
                return True
            return False
        (a, b) = sorted(C)
        if a == C[a] == 1:
            return True
        return True if C[b] == 1 and b - 1 == a else False

    def remove(B, x):
        if B[x] == 1:
            B.pop(x)
        else:
            B[x] -= 1

    B = Counter(nums)
    C = Counter(B.values())
    for i in reversed(range(len(nums))):
        if isvalid(C):
            return i + 1
        x = nums[i]
        remove(C, B[x])
        remove(B, x)
        if B[x]:
            C[B[x]] += 1
    return 0