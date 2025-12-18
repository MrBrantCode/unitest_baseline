"""
QUESTION:
Implement the `bitwise_and_count` function in Python that takes two integers as input and returns the number of bits that are set to 1 in their bitwise AND result. The function must not use any built-in functions or libraries.
"""

def bitwise_and_count(num1, num2):
    bitwise_and = num1 & num2  # Perform bitwise AND
    count = 0
    while bitwise_and > 0:
        if bitwise_and & 1:  # Check if the least significant bit is set to 1
            count += 1
        bitwise_and = bitwise_and >> 1  # Shift bitwise AND result to the right
    return count