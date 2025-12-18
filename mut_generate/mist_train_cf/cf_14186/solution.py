"""
QUESTION:
Write a function called "multiply" that takes two integers x and y as input and returns their product without using the multiplication operator or any built-in multiplication functions.
"""

def multiply(x, y):
    result = 0
    for i in range(abs(y)):
        result += abs(x)
    if (x < 0 and y < 0) or (x > 0 and y > 0):
        return result
    else:
        return -result