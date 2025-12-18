"""
QUESTION:
Write a function named `binary_to_decimal` that takes a binary string as input and returns its decimal integer equivalent without using built-in conversion functions or libraries. The function should use only basic arithmetic operations and loops. The input binary string can have up to 1 billion digits. The function should have a time complexity of O(n), where n is the number of digits in the binary string, and a space complexity of O(1). The function should also handle binary strings with leading zeros correctly.
"""

def entance(binary):
    decimal = 0
    power = 0
    
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '1':
            decimal += 2 ** power
        power += 1
    
    return decimal