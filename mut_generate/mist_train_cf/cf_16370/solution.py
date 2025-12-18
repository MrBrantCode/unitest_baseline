"""
QUESTION:
Write a function `fibonacci_sum(n)` that calculates the sum of the Fibonacci sequence up to the nth term, excluding any term that is divisible by 5. Assume the Fibonacci sequence starts with 0 and 1.
"""

def fibonacci_sum(n):
    # Initialize the sum and the first two Fibonacci numbers
    fib_sum = 0
    a, b = 0, 1

    # Iterate through the Fibonacci sequence up to the nth term
    for _ in range(n):
        # Check if the current Fibonacci number is not divisible by 5
        if a % 5 != 0:
            fib_sum += a
        # Generate the next Fibonacci number
        a, b = b, a + b

    return fib_sum