"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to the nth number. The function should take an integer `n` as input and return a list of integers representing the Fibonacci sequence. The input `n` is guaranteed to be a prime number and greater than or equal to 2.
"""

def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence