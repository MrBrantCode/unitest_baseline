"""
QUESTION:
Construct a function named `oct_to_bin_oct_complement` that takes an octal number as input, converts it to its binary representation, and then returns the one's complement form of that binary representation. The function should not handle conversion to the negabinary system, but instead, follow the one's complement notation for binary numbers.
"""

def oct_to_bin_oct_complement(octal_num):
    # First convert the octal number to a binary string
    binary = bin(int(str(octal_num), 8))[2:]
    
    # Then invert all the bits to get One's complement
    one_complement = ''.join('1' if bit == '0' else '0' for bit in binary)

    return one_complement