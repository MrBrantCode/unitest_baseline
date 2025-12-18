"""
QUESTION:
Develop a function named `compute_checksum(packet)` that calculates the CRC-32 checksum of a given data packet consisting of hexadecimal byte values. The function should take a list of hexadecimal strings as input, where each string represents a sequence of bytes. The function should return the CRC-32 checksum as a hexadecimal string.
"""

import binascii

def compute_checksum(packet):
    """
    Calculate the CRC-32 checksum of a given data packet consisting of hexadecimal byte values.

    Args:
        packet (list): A list of hexadecimal strings, where each string represents a sequence of bytes.

    Returns:
        str: The CRC-32 checksum as a hexadecimal string.
    """
    # Concatenate the packet data, convert to bytes and calculate crc32 checksum
    crc = binascii.crc32(binascii.a2b_hex(''.join(packet)))
    return '%08X' % (crc & 0xFFFFFFFF)