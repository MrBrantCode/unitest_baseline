"""
QUESTION:
Write a function named `arrayPairSum` that takes two parameters: a list of integers `nums` and an integer `k`. Group the integers in `nums` into `n` pairs `(a1, b1), (a2, b2), ..., (an, bn)` where `n` is half the length of `nums`, such that the sum of `min(ai, bi)` for all `i` is maximized and the absolute difference between `ai` and `bi` is less than or equal to `k`. Return the maximized sum.

Constraints:
- The length of `nums` is even and between 2 and 2 * 10^4.
- All elements in `nums` are between -10^4 and 10^4.
- `k` is between 0 and 10^4.
"""

def arrayPairSum(nums, k):
    nums.sort()
    i = 0
    res = 0
    while i < len(nums):
        if i + 1 < len(nums) and abs(nums[i+1] - nums[i]) <= k:
            res += nums[i]
            i += 2
        else:
            i += 1
    return res