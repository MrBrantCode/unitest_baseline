"""
QUESTION:
Write a function named `binary_to_decimal` that takes a string of binary digits (up to 1 million digits) as input and returns its decimal equivalent without using any built-in conversion functions or libraries. The function should only use basic arithmetic operations (addition, subtraction, multiplication, and division) and loops.
"""

def binary_to_decimal(binary_string):
    decimal = 0
    power = len(binary_string) - 1

    for digit in binary_string:
        if digit == '1':
            decimal += 2 ** power
        power -= 1

    return decimal