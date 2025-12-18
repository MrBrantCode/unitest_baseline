"""
QUESTION:
Create a function `generate_fibonacci(n)` that generates the Fibonacci sequence up to a given number `n`. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should return a list containing the Fibonacci sequence up to the given number `n`.
"""

def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1

    while a <= n:
        sequence.append(a)
        a, b = b, a + b

    return sequence