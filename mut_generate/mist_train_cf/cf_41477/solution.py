"""
QUESTION:
Write a function `closestSumPair(arr, target)` to find two distinct elements in the array `arr` whose sum is closest to the target value `target`. If there are multiple pairs with the same sum closest to the target, return the pair with the smallest sum.

The function takes a list of integers `arr` and a target value `target` as input, and returns a tuple of two integers representing the pair of elements whose sum is closest to the target. The list `arr` contains at least 2 elements and at most 10^5 elements, where each integer x is between -10^4 and 10^4. The target value `target` is an integer between -10^4 and 10^4.
"""

from typing import List, Tuple

def closestSumPair(arr: List[int], target: int) -> Tuple[int, int]:
    arr.sort()
    left, right = 0, len(arr) - 1
    closest_sum = float('inf')
    result = (arr[left], arr[right])

    while left < right:
        current_sum = arr[left] + arr[right]
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum
            result = (arr[left], arr[right])

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return result