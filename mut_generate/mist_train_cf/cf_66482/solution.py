"""
QUESTION:
Implement a function named `crc8` that takes a list of byte values in hexadecimal form and returns the calculated CRC-8 checksum using the CRC polynomial `x^8 + x^2 + x + 1` represented as `0x07`. The input data packet will only contain byte values. The calculated CRC-8 checksum should be returned as an integer value representing the checksum.
"""

def crc8(data):
    crc = 0
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = ((crc << 1) ^ 0x07) & 0xff
            else:
                crc <<= 1
    return crc