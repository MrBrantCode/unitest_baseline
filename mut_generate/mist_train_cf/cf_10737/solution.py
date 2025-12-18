"""
QUESTION:
Write a function `string_to_byte_array` that takes a string as input and returns the corresponding byte array. The function should only use bitwise operators (AND, OR, XOR, shift operators, etc.) to perform the conversion. Do not use built-in functions like `ord()` or `bytearray()`.
"""

def string_to_byte_array(s):
    byte_array = []
    for char in s:
        ascii_value = 0
        for i in range(8):
            ascii_value |= (ord(char) >> i & 1) << i
        byte_array.append(ascii_value)
    return byte_array