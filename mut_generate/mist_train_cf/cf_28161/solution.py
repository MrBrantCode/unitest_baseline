"""
QUESTION:
Implement a `substitute` function that takes a message and a shift value as input and returns the encrypted or decrypted message using a simple substitution cipher with the specified shift value. The function should shift each letter in the message by the specified number of positions in the alphabet while leaving non-alphabetic characters unchanged.
"""

def substitute(message, shift):
    """
    Encrypts or decrypts a message using a simple substitution cipher with the specified shift value.

    Args:
        message (str): The message to be encrypted or decrypted.
        shift (int): The number of positions to shift each letter in the message.

    Returns:
        str: The encrypted or decrypted message.
    """
    result = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26) + ord('a' if char.islower() else 'A'))
            result += shifted_char
        else:
            result += char
    return result