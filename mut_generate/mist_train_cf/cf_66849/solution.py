"""
QUESTION:
Create a function `encode_message(message)` to encode a given string message using a predefined codebook that maps characters to uncommon Unicode symbols, and another function `decode_message(encoded_message)` to decode the encoded message back to its original form. The codebook should map 'A' to '⚛', 'B' to '✡', 'C' to '☸', 'D' to '⚜', and 'E' to '♔'. The functions should be case-insensitive when matching characters to the codebook.
"""

def encode_message(message):
    codebook = {
        'A': '⚛',
        'B': '✡',
        'C': '☸',
        'D': '⚜',
        'E': '♔',
    }
    encoded_message = ''
    for char in message.upper():
        if char in codebook:
            encoded_message += codebook[char]
    return encoded_message

def decode_message(encoded_message):
    codebook = {
        '⚛': 'A',
        '✡': 'B',
        '☸': 'C',
        '⚜': 'D',
        '♔': 'E',
    }
    decoded_message = ''
    for char in encoded_message:
        if char in codebook:
            decoded_message += codebook[char]
    return decoded_message