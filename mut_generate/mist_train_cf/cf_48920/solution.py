"""
QUESTION:
Write a function named `fibn(n)` that generates and returns the first n Fibonacci numbers, where n is a positive integer and the Fibonacci sequence starts with 0 and 1. The function should not take any input other than n and should return the Fibonacci sequence as a list of integers.
"""

def fibn(n):
    sequence = []
    a = 0
    b = 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence