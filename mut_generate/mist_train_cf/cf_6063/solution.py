"""
QUESTION:
Design a recursive function called `fibonacci` that takes an integer `n` and returns the `n`th Fibonacci number. The function should handle negative input values by returning an error message. Implement memoization to optimize recursive calls. Do not use any loops or iteration constructs, and ensure the function has a time complexity of O(n) and a space complexity of O(n).
"""

def fibonacci(n, memo={}):
    if n < 0:
        return "Error: Negative input value"
    if n in memo:
        return memo[n]
    if n == 0:
        memo[n] = 0
        return 0
    elif n == 1:
        memo[n] = 1
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]