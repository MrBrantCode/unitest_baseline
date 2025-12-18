"""
QUESTION:
Create a function `caesar_cipher_encode(message, shift)` that encodes a message using the Caesar cipher encryption algorithm. The function should handle both uppercase and lowercase letters and non-alphabetical characters, and it should shift the letters by the specified shift value within the range of 1 to 26. The function should return the encoded message.
"""

def caesar_cipher_encode(message, shift):
    """
    Encodes a message using the Caesar cipher encryption algorithm.

    Args:
        message (str): The message to be encoded.
        shift (int): The shift value within the range of 1 to 26.

    Returns:
        str: The encoded message.
    """
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encoded_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encoded_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message