"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to `n` using recursion. The function should return a list of Fibonacci numbers. The function should handle cases where `n` is less than or equal to 0, 1, or 2. The function should not use any loops.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq