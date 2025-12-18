"""
QUESTION:
Write a function named `fibonacci` that generates the Fibonacci sequence up to the n-th term. The sequence should start with the fundamental term 1 and end at the n-th term. The function should be efficient and scalable for larger values of 'n'.
"""

def fibonacci(n):
    sequence = [1, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence