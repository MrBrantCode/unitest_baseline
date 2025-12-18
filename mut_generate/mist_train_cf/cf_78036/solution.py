"""
QUESTION:
Write a function `findClosestElements` that takes a sorted integer array `arr`, an integer `k`, and an integer `x` as input. The function should return the `k` integers in `arr` that are closest to `x`, in ascending order.

The proximity of an integer `a` to `x` is determined by the conditions: `|a - x| < |b - x|`, or `|a - x| == |b - x|` and `a < b`.

Constraints: `1 <= k <= arr.length`, `1 <= arr.length <= 10^4`, `arr` is sorted in ascending order, `-10^4 <= arr[i], x <= 10^4`. The solution should not use any built-in sorting functions and should have a time complexity of O(log n).
"""

def findClosestElements(arr, k, x):
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]