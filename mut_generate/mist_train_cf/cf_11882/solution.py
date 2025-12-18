"""
QUESTION:
Write a function called multiply that takes two positive integers, a and b, as input and returns their product without using the multiplication operator. The function should use a loop to perform the calculation by adding a to itself b times.
"""

def multiply(a, b):
    result = 0
    for i in range(b):
        result += a
    return result