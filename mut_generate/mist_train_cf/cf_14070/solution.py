"""
QUESTION:
Design a function called `fibonacci` that generates the Fibonacci sequence up to the nth number. The function should use a single loop, no recursion, and handle cases where n is less than or equal to 0 by returning an empty list.
"""

def fibonacci(n):
    # Handle edge case
    if n <= 0:
        return []

    # Initialize the Fibonacci sequence list
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_seq = [0, 1]

    # Loop to find the Fibonacci numbers
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])

    return fib_seq