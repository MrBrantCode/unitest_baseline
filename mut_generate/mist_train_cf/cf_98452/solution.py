"""
QUESTION:
Implement the Collatz Conjecture using a recursive function named `collatz(n, memo)` that takes a natural number `n` and a memoization dictionary `memo` as arguments. The function should return the stopping time of `n`, defined as the number of iterations required to reach the number 1 starting from `n`, using memoization to store previously computed intermediate numbers and avoid repeating calculations. The stopping time should be calculated based on the standard Collatz sequence rules: if `n` is even, the next number is `n//2`, and if `n` is odd, the next number is `3*n + 1`.
"""

def collatz(n, memo={1: 0}):
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        memo[n] = 1 + collatz(n//2, memo)
    else:
        memo[n] = 1 + collatz(3*n + 1, memo)
    return memo[n]