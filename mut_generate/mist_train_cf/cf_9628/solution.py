"""
QUESTION:
Design a function called "calculate_fibonacci" that takes an integer n as input and returns the Fibonacci sequence up to n. The function should handle negative inputs by returning an error message.
"""

def calculate_fibonacci(n):
    if n < 0:
        return "Error: n cannot be negative."

    fib_sequence = [0, 1]
    if n == 0:
        return []
    elif n == 1:
        return fib_sequence[:1]
    elif n == 2:
        return fib_sequence

    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence