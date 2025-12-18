"""
QUESTION:
Write a function `fib(n)` that calculates the `n`-th Fibonacci number using memoization, where `fib(n)` is defined as `fib(n-1) + fib(n-2)` with base cases `fib(0) = 0` and `fib(1) = 1`. The function should store the results of previously calculated Fibonacci numbers to avoid redundant calculations.
"""

def fib(n, memo = {}):
   if n <= 1:
       return n
   elif n not in memo:
       memo[n] = fib(n-1, memo) + fib(n-2, memo)
   return memo[n]