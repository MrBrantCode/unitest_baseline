"""
QUESTION:
Construct a function `maxValue` that takes three integers `n`, `index`, and `maxSum` as input and returns the maximum value at `nums[index]` from the array `nums` with length `n`. The array must satisfy the following conditions:

- The length of `nums` equals `n`.
- Each element `nums[i]` is a positive integer.
- The absolute difference between consecutive elements is less than or equal to 1.
- The total sum of all elements in `nums` does not surpass `maxSum`.
- The element at `nums[index]` is maximized.
- The array `nums` is a palindrome.
- The sum of elements at even indices is equal to the sum of elements at odd indices.
- The sum of elements at indices that are multiples of 3 is equal to the sum of elements at indices that are not multiples of 3.

Constraints: 
1 <= n <= maxSum <= 10^9
0 <= index < n
"""

def maxValue(n: int, index: int, maxSum: int) -> int:
    def test(a):
        b = max(a - index, 0)
        res = (a + b) * (a - b + 1) // 2
        b = max(a - ((n - 1) - index), 0)
        res += (a + b) * (a - b + 1) // 2
        return res - a

    maxSum -= n
    left, right = 0, maxSum
    while left < right:
        mid = (left + right + 1) // 2
        if test(mid) <= maxSum: left = mid
        else: right = mid - 1
    return left + 1