"""
QUESTION:
Write a function `fibonacci` that uses dynamic programming to efficiently calculate the nth Fibonacci number, and another function `fibonacci_sequence` that generates the first 10 numbers in the Fibonacci sequence. The `fibonacci` function should have a time complexity better than naive recursion and should not exceed the maximum recursion depth for large inputs. The `fibonacci_sequence` function should use `fibonacci` to generate the sequence.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 1:
        return n
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]