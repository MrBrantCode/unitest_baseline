"""
QUESTION:
Create a function `rot13_encode(text)` to encode a given text string using the ROT13 algorithm, preserving case sensitivity and non-alphabetic characters. Additionally, develop a corresponding function `rot13_decode(encoded_text)` to reverse the encoded string back to its original form. The function should handle both lowercase and uppercase letters, and any characters that are not letters should remain unchanged.
"""

def rot13_encode(text):
    """
    Encodes a given text string using the ROT13 algorithm, preserving case sensitivity and non-alphabetic characters.

    Args:
        text (str): The text to be encoded.

    Returns:
        str: The ROT13 encoded text.
    """

    encoded_text = []

    for char in text:
        if 'A' <= char <= 'Z':
            offset = ord('A')
            encoded_char = chr((ord(char) - offset + 13) % 26 + offset)
        elif 'a' <= char <= 'z':
            offset = ord('a')
            encoded_char = chr((ord(char) - offset + 13) % 26 + offset)
        else:
            encoded_char = char

        encoded_text.append(encoded_char)

    return ''.join(encoded_text)


def rot13_decode(encoded_text):
    """
    Decodes a given ROT13 encoded string back to its original form.

    Args:
        encoded_text (str): The text to be decoded.

    Returns:
        str: The decoded text.
    """

    decoded_text = []

    for char in encoded_text:
        if 'A' <= char <= 'Z':
            offset = ord('A')
            decoded_char = chr((ord(char) - offset - 13) % 26 + offset)
        elif 'a' <= char <= 'z':
            offset = ord('a')
            decoded_char = chr((ord(char) - offset - 13) % 26 + offset)
        else:
            decoded_char = char

        decoded_text.append(decoded_char)

    return ''.join(decoded_text)