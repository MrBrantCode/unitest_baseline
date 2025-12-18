"""
QUESTION:
Write a function `binary_to_decimal(binary_string)` that converts a given binary string to its corresponding decimal number without using any built-in functions or libraries for binary to decimal conversion. The function must have a time complexity of O(n), where n is the length of the binary string, and should handle binary strings containing only '0' and '1' characters.
"""

def binary_to_decimal(binary_string):
    decimal = 0
    for i in range(len(binary_string)):
        decimal = decimal + int(binary_string[i]) * 2**(len(binary_string) - i - 1)
    return decimal