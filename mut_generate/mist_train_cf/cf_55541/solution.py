"""
QUESTION:
Write a function `minAbsDifference(nums, goal)` that takes an array of integers `nums` and an integer `goal` as input. The function should return the smallest achievable value of `abs(sum - goal)`, where `sum` is the aggregate of elements in a subsequence of `nums`. A subsequence of an array is a new array created by excluding some elements (potentially all or none) from the original array.

Constraints: 
- `1 <= nums.length <= 40`
- `-10^7 <= nums[i] <= 10^7`
- `-10^9 <= goal <= 10^9`
"""

import bisect

def minAbsDifference(nums, goal):
    def get_sums(nums):
        sums = {0}
        for num in nums:
            sums |= {x + num for x in sums}
        return sorted(list(sums))

    mid = len(nums) // 2
    left, right = get_sums(nums[:mid]), get_sums(nums[mid:])

    res = float('inf')
    for l in left:
        i = bisect.bisect_right(right, goal - l)
        if i < len(right):
            res = min(res, right[i] + l - goal)
        if i > 0:
            res = min(res, goal - right[i-1] - l)
        if res == 0:
            return 0
    return res