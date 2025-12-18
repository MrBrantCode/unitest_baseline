"""
QUESTION:
Create a function named `base10_to_base16` that takes a single positive integer `num` as input and returns its equivalent hexadecimal (base 16) representation as a string. The function should handle the input number zero without entering an infinite loop.
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