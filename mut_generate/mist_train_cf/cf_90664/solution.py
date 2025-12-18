"""
QUESTION:
Write a function `fibonacci_memoization(n)` to generate the Fibonacci series up to the nth term using a recursive algorithm with memoization. The function should return a list of Fibonacci numbers. The input `n` is a non-negative integer, and the function should handle cases where `n` is 0, 1, or 2. The function should also use memoization to optimize its performance by storing and reusing previously calculated Fibonacci series.
"""

def fibonacci_memoization(n, memo={}):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        if n in memo:
            return memo[n]
        else:
            series = fibonacci_memoization(n-1, memo)
            series.append(series[-1] + series[-2])
            memo[n] = series
            return series