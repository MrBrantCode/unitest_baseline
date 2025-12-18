"""
QUESTION:
Create a function called `fibonacci(n)` that generates a Fibonacci sequence up to `n` elements using an iterative approach and dynamic programming. The function should not use recursion or the golden ratio formula. The function should return a list of the first `n` Fibonacci numbers. The input `n` is a non-negative integer.
"""

def fibonacci(n):
    if n <= 0:
        return []

    sequence = [0] * n
    sequence[0] = 0
    if n > 1:
        sequence[1] = 1

    for i in range(2, n):
        sequence[i] = sequence[i-1] + sequence[i-2]

    return sequence