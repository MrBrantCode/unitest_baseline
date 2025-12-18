"""
QUESTION:
Implement the Collatz Conjecture using a recursive function that returns the stopping time of a given natural number. The stopping time is defined as the number of iterations required to reach the number 1 starting from the given number. Use memoization to store previously computed intermediate numbers and avoid repeating calculations. The function should take a natural number `n` and a memoization dictionary `memo` as arguments and return the stopping time. The function should handle both even and odd numbers according to the Collatz Conjecture rules: if `n` is even, the next number is `n` divided by 2; if `n` is odd, the next number is 3 times `n` plus 1.
"""

def collatz(n, memo={1: 0}):
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        memo[n] = 1 + collatz(n//2, memo)
    else:
        memo[n] = 1 + collatz(3*n + 1, memo)
    return memo[n]