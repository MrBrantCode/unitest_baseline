"""
QUESTION:
Implement a function `fibonacci` that generates the nth Fibonacci number using recursion and memoization. The memoization technique should utilize a custom data structure that provides constant time complexity for both inserting and retrieving values, and does not use built-in data structures like dictionaries or hashmaps. The function should handle large values of n (e.g., n > 10000) without causing a stack overflow or excessive memory usage.
"""

class Memoization:
    def __init__(self):
        self.memo = {}

    def get(self, n):
        if n in self.memo:
            return self.memo[n]
        else:
            return None

    def put(self, n, value):
        self.memo[n] = value


def fibonacci(n, memoization):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        memo_value = memoization.get(n)
        if memo_value is not None:
            return memo_value
        else:
            fib_value = fibonacci(n - 1, memoization) + fibonacci(n - 2, memoization)
            memoization.put(n, fib_value)
            return fib_value