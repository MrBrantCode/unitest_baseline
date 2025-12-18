"""
QUESTION:
Determine the sum of the first 100 elements in the Fibonacci sequence. The Fibonacci sequence is defined as a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1. Write a function `fibonacci_sequence(n)` to solve this problem.
"""

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sum(sequence)