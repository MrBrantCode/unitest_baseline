"""
QUESTION:
Create a function named `convert_matrix` that takes a list of hexadecimal numbers as input and returns a list of their decimal equivalents. Each hexadecimal number is represented as a string and prefixed with '0x'. The function should work for any list of hexadecimal numbers.
"""

def convert_matrix(data):
    return [int(x, 16) for x in data]