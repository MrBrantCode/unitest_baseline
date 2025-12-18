"""
QUESTION:
Write a function `decode_bitwise_xor` that can reverse the effect of multiple `bitwise_xor` operations on a string. The `bitwise_xor` function performs a bitwise XOR operation with a key on each character in the string. The decoding function should be able to handle strings that have been encoded multiple times with different keys. The keys used for encoding are incremental, starting from a given initial key. The function should be able to decode strings containing symbols and whitespaces.
"""

def decode_bitwise_xor(s: str, key_start: int, times: int):
    """
    Decodes a string that has been encoded multiple times using different keys, 
    so long as the initial key is known and the string was encoded using incrementing keys.
    """
    for i in range(times-1, -1, -1):
        s = "".join([chr(ord(char) ^ (key_start+i)) for char in s])

    return s