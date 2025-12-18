"""
QUESTION:
Write a function named `number_properties` that takes two positive integers `num1` and `num2` as input. The function should calculate the sum of the two numbers and then print out the following properties of the sum:
- Whether the sum is even or odd.
- Whether the sum is a prime number.
- Whether the sum is a perfect square.
- Whether the sum is a Fibonacci number.
- Whether the sum is divisible by both `num1` and `num2`, by one of them, or by neither.
The function should handle cases where either of the numbers is zero or the sum exceeds 1,000,000.
"""

import math

def number_properties(num1, num2):
    """
    Calculate the sum of two numbers and print its properties.
    
    Parameters:
    num1 (int): The first positive integer.
    num2 (int): The second positive integer.
    """
    
    # Check if either of the numbers is zero
    if num1 == 0 or num2 == 0:
        print("One of the numbers is zero.")
        return

    # Check if the sum exceeds the limit
    if num1 + num2 > 1000000:
        print("The sum exceeds the limit.")
        return

    # Calculate the sum
    total = num1 + num2

    # Check if the sum is even or odd
    if total % 2 == 0:
        print("The sum is even.")
    else:
        print("The sum is odd.")

    # Check if the sum is prime
    if total > 1 and all(total % i for i in range(2, int(math.sqrt(total)) + 1)):
        print("The sum is a prime number.")

    # Check if the sum is a perfect square
    sqrt = int(math.sqrt(total))
    if sqrt * sqrt == total:
        print("The sum is a perfect square.")

    # Check if the sum is a Fibonacci number
    a, b = 0, 1
    while b < total:
        a, b = b, a + b
    if b == total:
        print("The sum is a Fibonacci number.")

    # Check if the sum is divisible by both numbers
    if total % num1 == 0 and total % num2 == 0:
        print("The sum is divisible by both numbers.")
    elif total % num1 == 0 or total % num2 == 0:
        print("The sum is divisible by one of the numbers.")
    else:
        print("The sum is not divisible by either of the numbers.")