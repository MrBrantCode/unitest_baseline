"""
QUESTION:
Write a function `toHex(num: int) -> str` that takes an integer `num` as input and returns its hexadecimal representation as a string. The function should use bitwise operations only and have a time complexity of O(log n). The function should be implemented using a recursive algorithm.
"""

def toHex(num: int) -> str:
    if num == 0:
        return "0"

    hex_digits = "0123456789abcdef"
    
    def toHexHelper(n: int) -> str:
        if n == 0:
            return ""
        
        remainder = n & 15
        hex_digit = hex_digits[remainder]
        
        return toHexHelper(n >> 4) + hex_digit if n > 15 else hex_digit
    
    return toHexHelper(num)