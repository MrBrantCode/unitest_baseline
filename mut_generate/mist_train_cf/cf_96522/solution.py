"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci series up to the given number `n` using recursion. The time complexity should be O(n) and the space complexity should be O(1), excluding the space used for the output. The function should handle the edge cases where `n` is 0, 1, or 2, and should not use any loops or helper functions.
"""

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = fibonacci(n - 1)
        series.append(series[-1] + series[-2])
        return series