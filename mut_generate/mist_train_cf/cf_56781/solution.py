"""
QUESTION:
You are given a function `maxValue` that takes three integers as input: `n`, `index`, and `maxSum`, where `n` is the length of the array, `index` is the index at which the maximum value should be obtained, and `maxSum` is the maximum sum of all elements in the array. The function should return the maximum possible value at `index` in a palindrome array where the absolute difference between adjacent elements is at most 1 and the sum of all elements does not exceed `maxSum`.
"""

def maxValue(n: int, index: int, maxSum: int) -> int:
    def test(a: int) -> bool:
        b = max(a - index, 0)
        res = (a + b) * (a - b + 1) // 2
        b = max(a - ((n - 1) - index), 0)
        res += (a + b) * (a - b + 1) // 2
        return res - a <= maxSum

    res = 1
    l, r = 1, maxSum
    while l <= r:
        mid = (l + r) // 2
        if test(mid):
            res = mid
            l = mid + 1
        else:
            r = mid - 1
    return res