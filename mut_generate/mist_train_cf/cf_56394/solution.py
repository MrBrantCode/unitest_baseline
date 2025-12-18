"""
QUESTION:
Write a function `maxNonOverlapping(nums, target)` that takes an array of integers `nums` and an integer `target` as input. Return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to `target`, along with all possible sets of non-overlapping subarrays.

Constraints:
- The length of `nums` is between 1 and 10^5.
- Each element in `nums` is between -10^4 and 10^4.
- The value of `target` is between 0 and 10^6.
"""

def maxNonOverlapping(nums, target):
    left = 0
    total_sum = 0
    res = []
    sub = []
    for right in range(len(nums)):
        total_sum += nums[right]
        sub.append(nums[right])
        while total_sum > target:
            total_sum -= nums[left]
            sub.pop(0)
            left += 1
        if total_sum == target:
            res.append(sub[:])
            left = right + 1
            total_sum = 0
            sub = []
    return len(res), res