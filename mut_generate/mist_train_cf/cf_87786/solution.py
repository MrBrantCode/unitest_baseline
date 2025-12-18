"""
QUESTION:
Write a function named `binary_to_decimal` that takes a binary string as input and returns its decimal equivalent as an integer. The function should not use any built-in conversion functions or libraries. It can only use basic arithmetic operations (addition, subtraction, multiplication, and division) and loops. The function should handle binary strings with up to 1 billion digits and should have a time complexity of O(n), where n is the number of digits in the binary string. The space complexity should be O(1), meaning it cannot use additional data structures to store intermediate values. The function should also handle binary strings with leading zeros.
"""

def entance(binary):
    decimal = 0
    power = 0
    
    for i in range(len(binary)-1, -1, -1):
        if binary[i] == '1':
            decimal += 2 ** power
        power += 1
    
    return decimal