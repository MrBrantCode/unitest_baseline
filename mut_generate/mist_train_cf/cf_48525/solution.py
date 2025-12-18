"""
QUESTION:
Create a function named `fibonacci` that generates a sequence of the initial `n` elements from the Fibonacci series. The function should take an integer `n` as input and return a list of the first `n` Fibonacci numbers. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1.
"""

def fibonacci(n):
    sequence = [0, 1]  # The first two elements are always 0 and 1
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])  
    return sequence