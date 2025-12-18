"""
QUESTION:
Implement the function `calculate_S_u_k(u, k)` to calculate the cumulative sum of the highest divisor count within a sliding window of size `k` for the range `1` to `u`. The divisor count for a number `n` is defined as the number of divisors of `n`. The function should return the cumulative sum `S(u, k)`. The input values of `u` and `k` are guaranteed to be positive integers, and `u` is guaranteed to be greater than or equal to `k`.
"""

def calculate_S_u_k(u, k):
    n = [1] * (u + 1)
    for i in range(2, u + 1):
        for j in range(i, u + 1, i):
            n[j] += 1

    maximum = 0
    for i in range(k):
        if n[i] > maximum:
            maximum = n[i]

    s = maximum
    for i in range(k, u + 1):
        if n[i] > maximum:
            maximum = n[i]
        s += maximum

    return s