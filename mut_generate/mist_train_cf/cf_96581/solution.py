"""
QUESTION:
Create a function named `fibonacci` to calculate the nth Fibonacci number where n is a positive integer. The function should have a time complexity of O(log n) and a space complexity of O(1), and should not use recursion or any built-in functions for calculating exponents.
"""

def fibonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 0

    # Initialize the first two Fibonacci numbers
    fib_n_2 = 0  # F(0)
    fib_n_1 = 1  # F(1)

    # Use a loop to calculate the nth Fibonacci number
    for _ in range(2, n):
        # Calculate the next Fibonacci number using the formula F(n) = F(n-1) + F(n-2)
        fib_n = fib_n_1 + fib_n_2
        fib_n_2, fib_n_1 = fib_n_1, fib_n

    return fib_n_1