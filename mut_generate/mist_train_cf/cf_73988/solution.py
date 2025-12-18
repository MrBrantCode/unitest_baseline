"""
QUESTION:
Write a function `decode_bitwise_xor(s: str)` that accepts a string `s` encoded with the `bitwise_xor` function, where each character in the string is XORed with the number 123. The function should return the decoded string, correctly handling symbols, whitespace, and other special characters.
"""

def decode_bitwise_xor(s: str):
    """
    Decodes a bitwise XOR encoded string back to its original state, managing symbols and whitespace.
    """
    decoded_string = ""
    for char in s:
        # XORing the encoded character twice with the same number yields the original character
        decoded_string += chr(ord(char) ^ 123)  

    return decoded_string