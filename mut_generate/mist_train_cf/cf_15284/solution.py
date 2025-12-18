"""
QUESTION:
Implement a function `sqrt_rounded(n)` that calculates the square root of a given positive integer `n` and rounds it to the nearest integer, where `n` is less than or equal to 10^9. The solution should have a time complexity of O(log(N)), where N is the input number.
"""

def sqrt_rounded(n):
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2

        if mid * mid == n:
            return mid
        elif mid * mid > n:
            right = mid - 1
        else:
            left = mid + 1

    return right