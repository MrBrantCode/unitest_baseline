"""
QUESTION:
Write a function `fibonacci(n, memo={})` that generates the nth Fibonacci number efficiently using memoization to handle large inputs. The function should take two parameters: `n`, the position of the Fibonacci number to generate, and `memo`, a dictionary to store previously calculated Fibonacci numbers (defaulting to an empty dictionary). The function should return the nth Fibonacci number.
"""

def fibonacci(n, memo={}):
    if n in memo: 
        return memo[n]
    if n <= 2: 
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]