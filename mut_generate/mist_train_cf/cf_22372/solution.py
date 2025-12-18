"""
QUESTION:
Write a function called `decimal_to_binary` that takes a non-negative decimal integer `n` as input and returns its binary equivalent as a string. The function should have a time complexity of O(log^2 n), where n is the decimal value.
"""

def decimal_to_binary(n):
    # Find the most significant bit position
    msb = 0
    while (1 << msb) <= n:
        msb += 1

    # Convert the decimal to binary
    binary = ""
    for i in range(msb - 1, -1, -1):
        if (1 << i) & n:
            binary += "1"
        else:
            binary += "0"

    return binary