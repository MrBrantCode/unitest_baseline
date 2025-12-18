"""
QUESTION:
Create a function `fibonacci(n)` that calculates the nth number in the Fibonacci series, where each number is the sum of the previous two numbers in the sequence. The function should take a single integer argument `n` and return the corresponding value in the series. Assume `n` is a positive integer greater than 0.
"""

def fibonacci(n):
    if n <= 0:
        print("Input should be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b