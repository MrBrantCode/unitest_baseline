"""
QUESTION:
Implement the functions `caesar_cipher`, `reverse_caesar_cipher`, and `encryption_check` with the following requirements:

- The `caesar_cipher` function should take a string message and a shift key as input, and return the encrypted message by shifting all alphabetic characters by the shift key's magnitude while maintaining the original character case, punctuation, and spaces.
- The `reverse_caesar_cipher` function should take the encrypted message and the shift key as input, and return the decrypted message.
- The `encryption_check` function should take the original message, the encrypted message, and the shift key as input, and return a boolean value indicating whether the encryption and decryption processes were successful.
- The functions should handle shift keys beyond the range of 26 (alphabet letters count) by continuing the cycle from the beginning of the alphabet.
- Non-alphabetic characters should remain unchanged in the encrypted and decrypted messages.
"""

def caesar_cipher(message, shift):
    """
    Encrypts the given message by shifting all alphabetic characters by the shift key's magnitude while maintaining the original character case, punctuation, and spaces.

    Args:
        message (str): The input message to be encrypted.
        shift (int): The shift key for encryption.

    Returns:
        str: The encrypted message.
    """
    encrypted = ""
    unchanged_chars = " ,.!?/\[]{}():;-_+=@#^&*<>|~`$%0123456789"
    for char in message:
        if char in unchanged_chars:
            encrypted += char
        else:
            ascii_offset = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
    return encrypted

def reverse_caesar_cipher(encrypted, shift):
    """
    Decrypts the given encrypted message by shifting all alphabetic characters back by the shift key's magnitude while maintaining the original character case, punctuation, and spaces.

    Args:
        encrypted (str): The encrypted message to be decrypted.
        shift (int): The shift key for decryption.

    Returns:
        str: The decrypted message.
    """
    decrypted = ""
    unchanged_chars = " ,.!?/\[]{}():;-_+=@#^&*<>|~`$%0123456789"
    for char in encrypted:
        if char in unchanged_chars:
            decrypted += char
        else:
            ascii_offset = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
    return decrypted

def encryption_check(original, encrypted, shift):
    """
    Checks if the encryption and decryption processes were successful by comparing the original message with the decrypted message.

    Args:
        original (str): The original message.
        encrypted (str): The encrypted message.
        shift (int): The shift key used for encryption.

    Returns:
        bool: True if the encryption and decryption processes were successful, False otherwise.
    """
    return original == reverse_caesar_cipher(encrypted, shift)