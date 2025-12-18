"""
QUESTION:
Write a function `extract_version(header: bytes) -> int` that takes a bytes object `header` representing a network packet header, where the header starts with a 16-bit version field in big-endian format, and returns the version number as an integer.
"""

def extract_version(header: bytes) -> int:
    version_bytes = header[:2]  # Extract the first 16 bits for the version field
    version_number = int.from_bytes(version_bytes, byteorder='big')  # Convert the bytes to an integer
    return version_number