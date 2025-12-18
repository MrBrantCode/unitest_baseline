"""
QUESTION:
Create a function called `fibonacci` that generates a Fibonacci sequence up to `n` elements using an iterative approach and dynamic programming. The function should not use recursion or the golden ratio formula. The function should return a list of integers representing the Fibonacci sequence. The input `n` is a non-negative integer, where `n` represents the number of elements in the Fibonacci sequence. If `n` is 0 or less, the function should return an empty list.
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