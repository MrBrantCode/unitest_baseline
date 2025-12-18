"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to the `n`th number. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. The function should return a list of integers representing the Fibonacci sequence.
"""

def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence