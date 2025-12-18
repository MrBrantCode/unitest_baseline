"""
QUESTION:
Write a function named `tesseract_volume` that calculates the volume of a four-dimensional hypercube given its side length without using built-in power or multiplication functions. The function should take an integer `side_length` as input and return the volume as an integer.
"""

def multiply(x, y):
    result = 0
    for _ in range(y):
        result += x
    return result

def power(base, exp):
    result = 1
    for _ in range(exp):
        result = multiply(result, base)
    return result

def tesseract_volume(side_length):
    return power(side_length, 4)