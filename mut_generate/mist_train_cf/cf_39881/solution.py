"""
QUESTION:
Create a function called `crc7_mmc` that takes a string as input and returns the CRC-7/MMC checksum in both hexadecimal and binary formats. The CRC-7/MMC algorithm uses a polynomial of 0x09 (x^7 + x^3 + 1) for the computation and produces a 7-bit checksum. The function should return a tuple of two strings: the hexadecimal checksum as a 2-digit string and the binary checksum as a 7-bit string.
"""

def crc7_mmc(input_str):
    crc = 0
    poly = 0x09  # CRC-7/MMC polynomial

    for char in input_str:
        crc ^= ord(char)
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
            crc &= 0x7F  # Keep only 7 bits

    hex_checksum = format(crc, '02X')  # Convert to 2-digit hexadecimal string
    bin_checksum = format(crc, '07b')  # Convert to 7-bit binary string

    return hex_checksum, bin_checksum