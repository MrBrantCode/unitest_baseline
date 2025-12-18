"""
QUESTION:
Write a function `base10_to_base16` that takes a non-negative integer as input and returns its hexadecimal representation as a string. The function should handle the case where the input number is zero.
"""

def base10_to_base16(num):
    if num == 0:
        return '0'
    
    hex_chars = "0123456789ABCDEF"
    result = ""
    
    while num > 0:
        remainder = num % 16
        result = hex_chars[remainder] + result
        num = num // 16
    
    return result