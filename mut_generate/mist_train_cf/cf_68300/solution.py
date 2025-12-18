"""
QUESTION:
Write a function `gcd(num1, num2)` that calculates the greatest common divisor of two given integers using the Euclidean Algorithm. The function should handle both positive and negative integers.
"""

def entrance(num1, num2):
    num1 = abs(num1)  # Convert to absolute value if negative
    num2 = abs(num2)  # Convert to absolute value if negative

    while num2 != 0:
        num1, num2 = num2, num1 % num2

    return num1