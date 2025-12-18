"""
QUESTION:
Given an integer array `nums` of `2n` integers, group these integers into `n` pairs `(a1, b1), (a2, b2), ..., (an, bn)` such that the sum of `max(ai, bi)` for all `i` is minimized. The function should be named `arrayPairSum` and take `nums` as the input. The length of `nums` is `2 * n`, where `1 <= n <= 10^4` and `-10^4 <= nums[i] <= 10^4`.
"""

def arrayPairSum(nums):
    return sum(sorted(nums)[::2])