"""
QUESTION:
Write a function called `fibonacci(n)` that generates the Fibonacci sequence up to the nth term. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the previous two terms. The function should return the Fibonacci sequence as a list. The input `n` is a positive integer representing the number of terms in the sequence.
"""

def fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence