"""
QUESTION:
Implement a function named `binomialCoefficient(n, k)` to compute the binomial coefficient of two given integers `n` and `k`, where `n` is a positive integer greater than or equal to `k`. The function should return the binomial coefficient value modulo 10^9+7.
"""

def binomialCoefficient(n, k):
    if k > n - k:
        k = n - k

    coefficient = 1
    for i in range(1, k + 1):
        coefficient *= n - i + 1
        coefficient //= i
        coefficient %= 1000000007

    return coefficient