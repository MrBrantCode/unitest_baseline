"""
QUESTION:
Implement a function `closest_value(arr: List[int], target: int) -> int` that takes a sorted list of integers `arr` and a target value `target` as input, and returns the closest value to the target in the list. If there are multiple closest values, return the smallest one. The list has at most 10^5 elements, and each integer in the list is between -10^9 and 10^9. The target value is also an integer between -10^9 and 10^9.
"""

from typing import List

def closest_value(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    closest = arr[0]

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

        if abs(arr[mid] - target) < abs(closest - target) or (abs(arr[mid] - target) == abs(closest - target) and arr[mid] < closest):
            closest = arr[mid]

    return closest