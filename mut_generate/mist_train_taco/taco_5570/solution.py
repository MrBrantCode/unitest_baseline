"""
QUESTION:
In computing, there are two primary byte order formats: big-endian and little-endian. Big-endian is used primarily for networking (e.g., IP addresses are transmitted in big-endian) whereas little-endian is used mainly by computers with microprocessors.

Here is an example (using 32-bit integers in hex format):

Little-Endian: 00 6D F4 C9 = 7,206,089

Big-Endian:    C9 F4 6D 00 = 3,388,239,104

Your job is to write a function that switches the byte order of a given integer. The function should take an integer n for the first argument, and the bit-size of the integer for the second argument. The bit size must be a power of 2 greater than or equal to 8. Your function should return a None value if the integer is negative, if the specified bit size is not a power of 2 that is 8 or larger, or if the integer is larger than the specified bit size can handle. In this kata, assume that all integers are unsigned (non-negative) and that all input arguments are integers (no floats, strings, None/nil values, etc.). Remember that you will need to account for padding of null (00) bytes.

Hint: bitwise operators are very helpful! :)
"""

def switch_endian(n, bits):
    # Check if the integer is negative
    if n < 0:
        return None
    
    # Check if the bit size is a power of 2 and >= 8
    if bits < 8 or (bits & (bits - 1)) != 0:
        return None
    
    # Check if the integer is larger than the specified bit size can handle
    if n >= (1 << bits):
        return None
    
    out = 0
    while bits > 7:
        bits -= 8
        out <<= 8
        out |= n & 255
        n >>= 8
    
    return out if n == 0 and bits == 0 else None