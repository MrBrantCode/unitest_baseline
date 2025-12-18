"""
QUESTION:
Given three positive integers `n`, `index`, and `maxSum`, find the maximum value at `index` in a bounded array of length `n` where each element is a positive integer, the absolute difference between adjacent elements does not exceed 1, the sum of all elements does not exceed `maxSum`, and the array is a palindrome.
"""

def maxValue(n: int, index: int, maxSum: int) -> int:
    def minSum(V: int) -> int:
        l = max(0, V - index)
        r = max(0, V - ((n - 1) - index))
        ans = (V + l) * (V - l + 1) // 2 + (V + r) * (V - r + 1) // 2 - V
        return ans
    left, right = 1, maxSum
    while left < right:
        mid = (left + right + 1) // 2
        if minSum(mid) <= maxSum:
            left = mid
        else:
            right = mid - 1
    return right