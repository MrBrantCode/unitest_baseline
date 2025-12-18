"""
QUESTION:
Write a function named `count_ones_zeros` that takes an integer `num` as input. The function should return a string containing the 16-bit binary representation of the number, the number of ones in the binary representation, and the number of zeros. The input number must be non-negative and will be in the range -32768 to 32767 (inclusive). If the number is negative, return the error message "Error: Negative numbers are not allowed."
"""

def count_ones_zeros(num):
    if num < 0:
        return "Error: Negative numbers are not allowed."
    
    binary = bin(num & 0xffff)[2:].zfill(16)
    ones = binary.count('1')
    zeros = binary.count('0')
    
    return f"Binary representation: {binary}\nNumber of ones: {ones}\nNumber of zeros: {zeros}"