"""
QUESTION:
Create a function named `hex_to_twos_complement` that takes a hexadecimal string `hex_num` as input. The function should return the 32-bit binary representation of the input hexadecimal number in two's complement format. If the input hexadecimal number represents a negative integer, its binary representation should have a leading 1; otherwise, it should have a leading 0. The binary string should be padded with leading zeros if necessary to ensure it is 32 characters long.
"""

def hex_to_twos_complement(hex_num):
    # Convert the hex into a signed integer
    int_num = int(hex_num, 16)
    # If the number is negative, make it positive and calculate as normal,
    # and manually flip the most significant bit at the end.
    if int_num >= 2**31:
        binary = bin(int_num - 2**32)[2:]
        binary = '1' + binary.zfill(31)
    else:
        binary = bin(int_num)[2:]
        binary = binary.zfill(32)
    return binary