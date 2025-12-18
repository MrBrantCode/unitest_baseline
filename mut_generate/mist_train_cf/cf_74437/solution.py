"""
QUESTION:
Given a binary number, write a function named `count_zeros` that returns the count of null bits (zeros) in the binary numeral. The input will be an integer representing the binary number.
"""

def count_zeros(binary_num):
    count = 0
    for digit in str(binary_num):
        if digit == '0':
            count += 1
    return count