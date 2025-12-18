"""
QUESTION:
Write a function named `factorial(n)` to calculate the factorial of a given positive integer `n` (where 0 ≤ n ≤ 100) using recursion, with a time complexity less than O(n^2).
"""

def entance(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * entance(n-1)