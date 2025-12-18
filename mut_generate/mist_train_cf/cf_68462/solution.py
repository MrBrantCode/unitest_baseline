"""
QUESTION:
Compute the harmonic sum of n-1 using recursion with memoization. Create a function `harmonic_sum(n, memo={0:0.0})` that takes two parameters: `n` and an optional dictionary `memo` to store previously computed harmonic numbers. The function should handle edge cases where `n` is less than or equal to 0. The function should also be optimized for larger inputs using memoization, with a time complexity of O(n) and space complexity of O(n).
"""

def entance(n, memo = {0:0.0}):
    if n <= 0:
        return 0
    if n not in memo:
        memo[n] = entance(n-1, memo) + 1/n
    return memo[n]