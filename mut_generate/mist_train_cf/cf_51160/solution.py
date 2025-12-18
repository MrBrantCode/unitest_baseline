"""
QUESTION:
Implement a function `compress(num, shift)` that uses bitwise operations to compress an integer `num` by shifting its bits to the right by `shift` places. Then, implement a corresponding function `decompress(num, shift)` to retrieve the original integer by shifting the compressed bits back to the left by `shift` places. The compressed integer should be lossy, meaning significant bits may be removed if the original integer does not have trailing zeros in its binary representation.
"""

def compress(num, shift):
    """
    Compress an integer by shifting its bits to the right.

    Args:
    num (int): The number to compress.
    shift (int): The number of places to shift.

    Returns:
    int: The compressed number.
    """
    return num >> shift


def decompress(num, shift):
    """
    Decompress an integer by shifting its bits to the left.

    Args:
    num (int): The number to decompress.
    shift (int): The number of places to shift.

    Returns:
    int: The decompressed number.
    """
    return num << shift