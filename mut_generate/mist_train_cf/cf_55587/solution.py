"""
QUESTION:
Create a test suite for the function `addTwoNumbers(a, b)` that takes two numbers (integers or floating-point numbers) as input and returns their sum accurate to two decimal places. The test suite should cover the following cases: adding two integers, adding two floating-point numbers, and adding an integer and a floating-point number.
"""

def addTwoNumbers(a, b):
    return round(a + b, 2)