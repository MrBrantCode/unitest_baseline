"""
QUESTION:
Implement a function named `fibonacci_memo` that generates the Fibonacci sequence up to a given number `n` using memoization for optimization. The function should have a time complexity of O(n) and handle large numbers efficiently without causing memory overflow or excessive runtime. The function should return a list of Fibonacci numbers.
"""

def fibonacci_memo(n, memo={}):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    if n in memo:
        return memo[n]

    fib_sequence = fibonacci_memo(n-1, memo)
    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    memo[n] = fib_sequence

    return fib_sequence