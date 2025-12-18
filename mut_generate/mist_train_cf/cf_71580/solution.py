"""
QUESTION:
Create a function called binary_to_decimal that takes a string representing a binary number as input and returns its decimal equivalent. The input string will only contain the characters '0' and '1'. The function should not use any built-in binary conversion functions.
"""

def binary_to_decimal(binary_num):
    decimal_num = 0
    for i in range(len(binary_num)):
        decimal_num += int(binary_num[len(binary_num) - 1 - i]) * (2 ** i)
    return decimal_num