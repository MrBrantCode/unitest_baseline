"""
QUESTION:
Create a function named `fibonacci(n)` that generates the Fibonacci sequence iteratively using a loop, where `n` is the number of Fibonacci numbers to generate. The function should return a list of integers representing the first `n` Fibonacci numbers. The input `n` is a non-negative integer, and the function should handle cases where `n` is less than or equal to 2.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            next_number = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_number)
        return fib_sequence