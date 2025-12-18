"""
QUESTION:
Develop a function `crc8(data)` that calculates the CRC-8 checksum of a given data packet containing hexadecimal byte values. The function should use the polynomial x^8+x^2+x^1+1 (0x07). The input `data` is a list of integers representing the hexadecimal byte values, and the output should be the calculated CRC-8 checksum. The output should be an integer representing the 8-bit CRC value.
"""

def crc8(data):
    POLYNOMIAL = 0x07
    crc = 0x00
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ POLYNOMIAL
            else:
                crc <<= 1
    return crc & 0xFF