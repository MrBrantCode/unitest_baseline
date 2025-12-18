"""
QUESTION:
Write a function named `decimal_to_binary` that takes an integer `n` as input and returns its binary representation as a string using only bitwise operations. The function should have a time complexity of O(log n) and should not use any built-in functions or libraries to convert the number to binary.
"""

def decimal_to_binary(n):
    binary = ""
    for i in range(31, -1, -1):
        if (n & (1 << i)) > 0:
            binary += "1"
        else:
            binary += "0"
    return binary