"""
QUESTION:
Create a function `fibonacci_generator(n)` that generates the Fibonacci series up to a given number `n`. The function should use a recursive helper function `fibonacci_recursive(n)` that calculates each Fibonacci number using recursion and memoization. The `fibonacci_generator(n)` function should then use a generator to yield each Fibonacci number one at a time.
"""

def fibonacci_generator(n):
    memo = {}

    def fibonacci_recursive(k):
        if k in memo:
            return memo[k]
        if k <= 1:
            result = k
        else:
            result = fibonacci_recursive(k-1) + fibonacci_recursive(k-2)
        memo[k] = result
        return result

    for i in range(n):
        yield fibonacci_recursive(i)