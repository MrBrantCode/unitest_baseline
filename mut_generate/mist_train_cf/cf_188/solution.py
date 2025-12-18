"""
QUESTION:
Implement the `binary_to_decimal` function, which converts a binary string to its corresponding decimal number without using any built-in functions or libraries for binary to decimal conversion. The function must have a time complexity of O(n), where n is the length of the binary string. The input binary string is expected to be a string of '0's and '1's, and the output should be the decimal equivalent of the input binary string.
"""

def binary_to_decimal(binary_string):
    decimal = 0
    for i in range(len(binary_string)):
        decimal = decimal + int(binary_string[i]) * 2**(len(binary_string) - i - 1)
    return decimal