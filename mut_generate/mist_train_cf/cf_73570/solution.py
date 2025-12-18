"""
QUESTION:
Create a function named "generate_crc32" that takes a bytes object as input and returns a hexadecimal string representing the 32-bit CRC checksum of the input. The output should be a zero-padded 8-character string in uppercase. Ensure the CRC value is a 32-bit number.
"""

import binascii

def generate_crc32(data):
    crc = binascii.crc32(data)
    return "%08X" % (crc & 0xFFFFFFFF)