"""
QUESTION:
Implement a function called `find_max` that takes three integers as input and returns the maximum value based on certain conditions. If the first integer is the largest and divisible by 3, return it. If the second integer is the largest and divisible by 5, return it. Otherwise, return the third integer.
"""

def find_max(num1, num2, num3):
    return num1 if (num1 > num2 and num1 > num3 and num1 % 3 == 0) else (num2 if (num2 > num1 and num2 > num3 and num2 % 5 == 0) else num3)