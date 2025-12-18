"""
QUESTION:
Write a function `closestToTarget(arr, target)` that finds the minimum possible value of `|func(arr, l, r) - target|` given an integer array `arr` and an integer `target`, where `func(arr, l, r)` is a mysterious function that returns the bitwise AND of all numbers in `arr` from index `l` to `r` (inclusive).

The function should take two parameters: `arr` and `target`, where `1 <= arr.length <= 10^5`, `1 <= arr[i] <= 10^6`, and `0 <= target <= 10^7`. The function should return the minimum possible value of `|func(arr, l, r) - target|`.
"""

def closestToTarget(arr, target):
    ans = float('inf')
    valid = {arr[0]}
    for num in arr:
        valid = {num & x for x in valid} | {num}
        ans = min(ans, min(abs(x - target) for x in valid))
    return ans