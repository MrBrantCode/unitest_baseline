"""
QUESTION:
Create a function named `fibonacci_sequence` that generates a Fibonacci sequence up to a given positive integer n. The sequence should be returned as a list and should not include the first number that is greater than or equal to n. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
"""

def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence