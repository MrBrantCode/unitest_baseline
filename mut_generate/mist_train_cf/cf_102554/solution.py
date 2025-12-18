"""
QUESTION:
Write a Python function `xor_binary_numbers(num1, num2)` that takes two binary numbers of the same length `n` as strings, where `n` is a power of 2, and returns a list of integers representing the exclusive OR (XOR) of the two binary numbers. The function should only use bitwise operators and have a time complexity of O(n).
"""

def xor_binary_numbers(num1, num2):
    # Pad the binary numbers with leading zeroes if necessary
    n = max(len(num1), len(num2))
    num1 = num1.zfill(n)
    num2 = num2.zfill(n)
    
    # Convert the binary numbers to integers
    num1 = int(num1, 2)
    num2 = int(num2, 2)
    
    # Perform XOR operation using bitwise XOR operator
    xor_result = num1 ^ num2
    
    # Convert the XOR result back to binary representation
    xor_binary = bin(xor_result)[2:].zfill(n)
    
    # Convert the binary representation to a list of integers
    xor_list = [int(bit) for bit in xor_binary]
    
    return xor_list