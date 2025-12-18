"""
QUESTION:
Create a function named `xor_encrypt` that takes a string `text` and an integer `key` as input, and returns an array of bytes representing the XOR encryption of the input string with the provided key. The function should use the XOR operation to ensure each byte in the original string is indirectly manipulable and maintains parity. The function should be able to handle any valid string and key as input.
"""

def xor_encrypt(text, key):
    return [x ^ key for x in text.encode()]