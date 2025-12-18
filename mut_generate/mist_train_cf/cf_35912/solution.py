"""
QUESTION:
Implement a function `long_write` that takes an integer as input and returns a byte string. For positive integers, the byte string should represent the integer in little-endian byte order. For negative integers, the byte string should represent the absolute value of the integer minus 1, also in little-endian byte order.
"""

def long_write(n):
    if n >= 0:
        return n.to_bytes((n.bit_length() + 7) // 8, byteorder='little')
    else:
        abs_value = abs(n) - 1
        return abs_value.to_bytes((abs_value.bit_length() + 7) // 8, byteorder='little')