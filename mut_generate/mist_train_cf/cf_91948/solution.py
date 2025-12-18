"""
QUESTION:
Write a function called "isEvenlyDivisible" that takes two integers as parameters. The function should return true if the first integer is evenly divisible by the second integer, and false otherwise. The function should handle division by zero cases.
"""

def isEvenlyDivisible(num1, num2):
    return num2 != 0 and num1 % num2 == 0