"""
QUESTION:
Write a function `binary_addition` that takes two binary strings as input, adds their corresponding decimal values, and returns the result as a binary string. The function should handle the conversion from binary to decimal and back to binary internally.
"""

def binary_addition(element1, element2):
    # Convert binary strings to integers
    integer1 = int(element1, 2)
    integer2 = int(element2, 2)

    # Add the integers
    sum_integers = integer1 + integer2

    # Convert the sum back to binary and return as string
    return bin(sum_integers)[2:]