"""
QUESTION:
Write a function `fibonacci(n)` that generates the Fibonacci sequence up to the nth term, where n is a positive integer less than or equal to 100. The function should handle large values of n efficiently without using recursion and have a space complexity that does not depend on the value of n.
"""

def fibonacci(n):
    if n <= 0:
        return []

    fibonacci_sequence = [0, 1]  # Initialize with the first two Fibonacci numbers

    if n <= 2:
        return fibonacci_sequence[:n]

    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i-2])
        
    return fibonacci_sequence