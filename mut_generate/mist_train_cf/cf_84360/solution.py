"""
QUESTION:
Write a function `fib(n)` that generates the nth Fibonacci number using memoization to efficiently handle large inputs. The function should be able to compute Fibonacci numbers up to the input value `n` without exceeding the default Python recursion limit.
"""

def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = result
    return result