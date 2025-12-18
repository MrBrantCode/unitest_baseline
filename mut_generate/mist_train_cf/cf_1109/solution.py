"""
QUESTION:
Write a function `fibonacci(n, memo={})` to generate the nth Fibonacci number using recursion and memoization. The function should handle negative input values for n by printing an error message and returning None if n is less than 0.
"""

def entance(n, memo={}):
    if n < 0:
        print("Error: n cannot be negative.")
        return None
    
    if n in memo:
        return memo[n]
    
    if n == 0:
        memo[n] = 0
        return 0
    elif n == 1:
        memo[n] = 1
        return 1
    
    memo[n] = entance(n-1, memo) + entance(n-2, memo)
    return memo[n]