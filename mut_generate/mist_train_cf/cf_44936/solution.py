"""
QUESTION:
Create a function named `catalan_numbers(n)` that calculates the nth Catalan number. The function should use dynamic programming to store and reuse previously computed Catalan numbers, achieving a time complexity of O(n^2). The input `n` is a non-negative integer.
"""

def catalan_numbers(n):
    # Table to store results of subproblems
    catalan = [0 for _ in range(n+1)]

    # Initialize first two values
    catalan[0] = 1
    if n > 0:
        catalan[1] = 1

    # Fill catalan[] in a bottom-up manner, using recursive formula 
    for i in range(2, n+1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]

    return catalan[n]