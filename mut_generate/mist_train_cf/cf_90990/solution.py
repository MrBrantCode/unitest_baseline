"""
QUESTION:
Create a function called "calculate_fibonacci" that calculates the Fibonacci sequence up to a given non-negative integer n and returns the sequence as a list. If n is negative, return the string "Error: n cannot be negative."
"""

def calculate_fibonacci(n):
    fib_sequence = []

    if n < 0:
        return "Error: n cannot be negative."

    if n == 0:
        return fib_sequence

    fib_sequence.append(0)

    if n == 1:
        return fib_sequence

    fib_sequence.append(1)

    if n == 2:
        return fib_sequence

    a = 0
    b = 1

    for _ in range(n - 2):
        next_num = a + b
        a = b
        b = next_num
        fib_sequence.append(next_num)

    return fib_sequence