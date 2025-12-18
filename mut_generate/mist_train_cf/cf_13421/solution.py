"""
QUESTION:
Write a function `gcd` that calculates the greatest common divisor of two positive integers `num1` and `num2`. The function should return the greatest common divisor. Additionally, write a function `check_relatively_prime` that checks if the two numbers are relatively prime (i.e., their greatest common divisor is 1) and returns a boolean value. Assume that the input numbers are positive integers. The function should handle cases where one or both of the numbers are equal to 1.
"""

def gcd(num1, num2):
    """Calculates the greatest common divisor of two positive integers."""
    if num1 == 1 or num2 == 1:
        return 1
    while num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num1

def check_relatively_prime(num1, num2):
    """Checks if two numbers are relatively prime."""
    return gcd(num1, num2) == 1