"""
QUESTION:
Create a function named `multiply` that takes two integers as input and returns their product without using the multiplication operator (*). The function should work for positive integers.
"""

def entance(x, y):
    result = 0
    for i in range(y):
        result += x
    return result