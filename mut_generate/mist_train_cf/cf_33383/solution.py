"""
QUESTION:
Implement the function `encodeVariableLength(value)` that takes a non-negative integer `value` as input and returns a byte stream representing the variable-length encoding of the input value, using 7 bits of each byte to represent the value and the most significant bit (MSB) as a continuation flag.
"""

def encodeVariableLength(value):
    byte_stream = bytearray()
    while value >= 0x80:
        byte_stream.append((value & 0x7F) | 0x80)
        value >>= 7
    byte_stream.append(value & 0x7F)
    return byte_stream