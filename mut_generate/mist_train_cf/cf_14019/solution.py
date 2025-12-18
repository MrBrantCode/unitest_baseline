"""
QUESTION:
Create a function named `calculate_combination` that takes two non-negative integers `n` and `k` as input and returns the combination of `n` elements taken `k` at a time. If `n` is smaller than `k`, return an error message "Invalid input: n should be greater than or equal to k". The function should handle cases where `k` is 0 or `k` is equal to `n`, and it should return the result as an integer.
"""

def calculate_combination(n, k):
    if n < k:
        return "Invalid input: n should be greater than or equal to k"
    elif k == 0 or k == n:
        return 1
    else:
        numerator = 1
        denominator = 1

        for i in range(1, min(k, n - k) + 1):
            numerator *= n - i + 1
            denominator *= i

        return numerator // denominator