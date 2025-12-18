"""
QUESTION:
Write a function called `generate_fibonacci(n)` that produces an array of n Fibonacci numbers without using recursion and with a time complexity of O(n), using a constant amount of extra space.
"""

def generate_fibonacci(n):
    # Check if n is 0 or negative
    if n <= 0:
        return []

    # Initialize an array to store the Fibonacci numbers
    fibonacci = [0] * n

    # Base cases
    fibonacci[0] = 0
    if n > 1:
        fibonacci[1] = 1

    # Generate the Fibonacci numbers
    for i in range(2, n):
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2]

    return fibonacci