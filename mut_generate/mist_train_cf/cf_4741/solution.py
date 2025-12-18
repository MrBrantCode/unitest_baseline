"""
QUESTION:
Create a function called `fibonacci_sequence(n)` that takes a positive integer `n` as input, generates the Fibonacci sequence up to `n` using an iterative approach, and prints the sequence in reverse order. The function should handle cases where `n` is a negative number or zero by printing an error message.
"""

def fibonacci_sequence(n):
    if n <= 0:
        print("N must be a positive integer.")
        return

    fib = [0, 1]  # Initial values of Fibonacci sequence

    # Generate Fibonacci sequence up to N
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])

    # Print Fibonacci sequence in reverse order
    for i in range(n, -1, -1):
        print(fib[i], end=" ")

    print()