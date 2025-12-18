"""
QUESTION:
Convert a given decimal number to its binary representation as a string, ensuring the binary string does not exceed 8 digits. The function should be named 'decimal_to_binary'.
"""

def decimal_to_binary(n):
    binary_str = ""
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n = n // 2
    return binary_str.zfill(8)