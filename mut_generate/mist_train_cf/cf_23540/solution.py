"""
QUESTION:
Write a function `decimal_to_binary(num)` that takes an integer `num` as input and returns a list of integers representing the binary form of the decimal number. The binary form should be represented in the order of most significant bit to least significant bit.
"""

def decimal_to_binary(num):
    binary = []

    while num > 0:
        binary.append(num%2)
        num //= 2
    binary.reverse()
    return binary