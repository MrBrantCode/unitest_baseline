"""
QUESTION:
Implement a function `countValidTriangles(nums)` to calculate the total number of valid triangles that can be formed from a given list of positive integers. A valid triangle is formed by selecting three integers from the list such that the sum of any two integers is greater than the third integer. The input list `nums` contains 0 < len(nums) <= 1000 positive integers.
"""

from typing import List

def countValidTriangles(nums: List[int]) -> int:
    nums.sort()
    count = 0

    for i in range(len(nums) - 2):
        k = i + 2
        for j in range(i + 1, len(nums) - 1):
            while k < len(nums) and nums[i] + nums[j] > nums[k]:
                k += 1
            count += k - j - 1

    return count