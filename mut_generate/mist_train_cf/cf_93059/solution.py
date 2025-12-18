"""
QUESTION:
Write a function called `calculate_combination` that calculates the number of combinations of `n` elements taken `k` at a time. The function should take two non-negative integers `n` and `k` as input and return the number of combinations. If `n` is smaller than `k`, the function should return the string "Invalid input: n should be greater than or equal to k".
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