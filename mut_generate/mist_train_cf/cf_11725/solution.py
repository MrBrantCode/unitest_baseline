"""
QUESTION:
Convert the given bytes into a string, where each byte is first converted into its corresponding ASCII character code and then multiplied by 2. The resulting ASCII character codes should be converted back into characters and concatenated to form the final string.

The function should take a bytes-like object as input. The function should return a string. The input bytes will be 11 bytes in length, but this length might be subject to change in the future.
"""

def entrance(byte_data: bytes) -> str:
    """
    Convert each byte in the given bytes-like object into its corresponding ASCII character code, 
    multiply it by 2, convert the resulting ASCII character code back into a character, 
    and concatenate all the characters to form a string.

    Args:
        byte_data (bytes): A bytes-like object.

    Returns:
        str: A string representation of the input bytes after multiplying each ASCII character code by 2.
    """
    return ''.join(chr(byte * 2) for byte in byte_data)