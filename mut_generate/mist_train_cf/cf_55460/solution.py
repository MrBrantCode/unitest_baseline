"""
QUESTION:
Write a function `G(n)` that calculates the value of the Golomb's self-describing sequence for a given number `n`. The function should be able to efficiently compute the sum of `G(n^3)` for `1 ≤ n < 10^6`. The function should be able to handle large inputs without using excessive memory or computation time.
"""

def G(n, cache={1: 1, 2: 2}):
    if n in cache:
        return cache[n]
    i = max(cache)
    while i < n:
        i += 1
        cache[i] = cache[i - cache[cache[i - 1]]] + 1
    return cache[n]