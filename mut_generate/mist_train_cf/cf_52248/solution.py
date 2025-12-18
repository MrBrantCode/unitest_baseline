"""
QUESTION:
Write a function `sliding_parity(binary_number)` that takes a binary number as a string and returns a list of integers representing the parity (XOR) of each 2-bit sliding window, moving from left to right. The binary number is at least 2 bits long.
"""

def sliding_parity(binary_number):
    result = []
    for i in range(len(binary_number) - 1):
        parity = int(binary_number[i]) ^ int(binary_number[i + 1])
        result.append(parity)
    return result