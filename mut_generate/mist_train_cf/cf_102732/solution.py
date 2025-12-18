"""
QUESTION:
Write a function `is_fibonacci(number)` that takes an integer `number` as input and returns `True` if the number is a Fibonacci number, and `False` otherwise. A Fibonacci number is a number that is a sum of two preceding numbers (1 and 1 by default) and the sequence appears as follows: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on.
"""

def is_fibonacci(number):
    # Base case
    if number == 0 or number == 1:
        return True

    # Initialize variables
    fib_1 = 0
    fib_2 = 1
    fib_sum = fib_1 + fib_2

    # Calculate Fibonacci numbers until fib_sum is less than or equal to the given number
    while fib_sum <= number:
        # Check if the given number is equal to the current Fibonacci number
        if fib_sum == number:
            return True
        
        # Update Fibonacci numbers
        fib_1 = fib_2
        fib_2 = fib_sum
        fib_sum = fib_1 + fib_2

    # If the given number is not equal to any Fibonacci number, return False
    return False