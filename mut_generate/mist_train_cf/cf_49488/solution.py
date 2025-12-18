"""
QUESTION:
Write a function `findClosestElements` that takes a sorted integer array `arr`, an integer `k`, and an integer `x` as input. Return the `k` integers in `arr` that are closest to `x` in ascending order. If two integers have the same proximity to `x`, the smaller integer is considered closer. The proximity of an integer `a` to `x` is determined by `|a - x|`. 

The function should satisfy the following constraints: `1 <= k < arr.length`, `1 <= arr.length <= 10^4`, and `-10^4 <= arr[i], x <= 10^4`.
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