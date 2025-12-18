"""
QUESTION:
Given a list of integers `nums` and an integer `threshold`, find the smallest divisor such that the sum of the quotients of each element in `nums` divided by the divisor is less than or equal to the `threshold`. The list `nums` contains 1 to 10^5 elements, each representing an integer value between 1 and 10^6. The `threshold` is an integer between 1 and 10^9. The function `smallest_divisor(nums, threshold)` should return the smallest divisor that satisfies the given condition.
"""

from typing import List

def smallest_divisor(nums: List[int], threshold: int) -> int:
    def condition(divisor) -> bool:
        return sum((num - 1) // divisor + 1 for num in nums) <= threshold

    lo, hi = 1, max(nums)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if condition(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo