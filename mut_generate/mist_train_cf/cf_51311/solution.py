"""
QUESTION:
Write a function `sum_of_consecutive_numbers(N)` that determines the number of methods to represent a given positive integer `N` as a sum of sequential positive integers. The function should return the count of such representations. The input `N` is restricted to `1 <= N <= 10^9`.
"""

def sum_of_consecutive_numbers(N):
    count = 0
    k = 1
    while k * (k + 1) <= 2 * N:
        if (N - (k * (k + 1)) // 2) % k == 0:
            count += 1
        k += 1
    return count