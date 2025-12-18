"""
QUESTION:
Write a function `decode_hex_string(hex_string: str) -> Tuple[int, int, int, int]` that takes a hexadecimal string as input. The string is composed of bytes representing a little-endian unsigned 32-bit integer for payload length, a little-endian unsigned 32-bit integer for timestamp, a little-endian unsigned 16-bit integer for sequence number, and a single byte of data. The function should return a tuple containing the extracted payload length, timestamp, sequence number, and data byte in that order.
"""

from typing import Tuple

def entance(hex_string: str) -> Tuple[int, int, int, int]:
    byte_data = bytes.fromhex(hex_string)
    payload_length = int.from_bytes(byte_data[0:4], byteorder='little')
    timestamp = int.from_bytes(byte_data[4:8], byteorder='little')
    sequence_number = int.from_bytes(byte_data[8:10], byteorder='little')
    data_byte = byte_data[10]
    return payload_length, timestamp, sequence_number, data_byte