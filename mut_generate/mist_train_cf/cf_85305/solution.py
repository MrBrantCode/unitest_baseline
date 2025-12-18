"""
QUESTION:
Write a function `lucas_fibonacci_product` that calculates the product of the 200th number in the Lucas sequence and the nth Fibonacci number. The function should take an integer `n` as input, representing the position of the Fibonacci number. The function should return the product of the two numbers. The function should be able to handle large values of `n`. Note that the function should use an iterative approach for calculating the Lucas number and Binet's formula for calculating the Fibonacci number.
"""

import math

def lucas_fibonacci_product(n):
    # Function to calculate n-th Lucas number
    def lucas(n):
        # Base cases
        if n == 0:
            return 2
        if n == 1:
            return 1
        # two starting numbers of Lucas sequence.
        a, b = 2, 1
        for _ in range(2, n+1):
            a, b = b, a+b
        return b

    # Function to calculate n-th Fibonacci number
    def fib(n):
        # Using Binet's formula
        phi = (1 + math.sqrt(5)) / 2
        return round((phi ** n) / math.sqrt(5))

    # Calculate the product of the 200th Lucas number and the nth Fibonacci number
    lucas_number = lucas(200)
    fibonacci_number = fib(n)
    return lucas_number * fibonacci_number