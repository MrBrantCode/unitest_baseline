"""
QUESTION:
Design a function `fibonacci_sequence(y)` that generates a Fibonacci sequence up to the given number `y`. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones. The function should return the sequence as a list of numbers. The sequence should stop when a number exceeds `y`.
"""

def fibonacci_sequence(y):
    sequence = []
    a, b = 0, 1
    while a <= y:
        sequence.append(a)
        a, b = b, a + b
    return sequence