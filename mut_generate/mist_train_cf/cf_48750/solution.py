"""
QUESTION:
Generate the Nth Fibonacci number using a function called `generate_fibonacci(n)`. The Fibonacci sequence is a series of numbers where each number after the first two is the sum of the two preceding ones (0, 1, 1, 2, 3, 5, 8, 13, 21, ...). The function should take a positive integer `n` as input and return the corresponding Fibonacci number. If `n` is not a positive integer, the function should return an error message.
"""

def generate_fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b