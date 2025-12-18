"""
QUESTION:
Implement a function named `binary_to_decimal` that takes a binary string of up to 1000 characters consisting of only 0s and 1s and returns its decimal equivalent. Do not use built-in functions or libraries for the conversion and achieve a time complexity of O(n), where n is the length of the binary string.
"""

def binary_to_decimal(binary):
    decimal = 0
    power = len(binary) - 1

    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1

    return decimal