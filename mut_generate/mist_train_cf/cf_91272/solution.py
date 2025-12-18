"""
QUESTION:
Create a function named `fibonacci_sequence` that generates a Fibonacci sequence of a given length `n`, where `n` is a prime number between 10 and 100. The function should return a list of integers representing the Fibonacci sequence of length `n`.
"""

def fibonacci_sequence(n):
    sequence = [0, 1]  

    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]  
        sequence.append(next_num)  

    return sequence