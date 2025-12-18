"""
QUESTION:
Write a function `isDivisibleBy5` that takes a binary number as a string and returns `True` if the decimal equivalent of the binary number is divisible by 5, and `False` otherwise.
"""

def isDivisibleBy5(binary): 
    decimal = 0
    for i, digit in enumerate(reversed(binary)):
        decimal += int(digit) * pow(2, i)
    return decimal % 5 == 0