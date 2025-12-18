"""
QUESTION:
Create a function named `find_maximum` that takes two numbers as input and returns the maximum of those numbers without using any built-in Python functions or operators for finding the maximum.
"""

def find_maximum(num1, num2):
    # Compare the numbers using if-else statements
    if num1 > num2:
        return num1
    else:
        return num2