"""
QUESTION:
Write a function called `caesar_cipher_encode` that takes a string message and an integer shift value as input and returns the encoded message using the Caesar cipher algorithm. The function should support both uppercase and lowercase letters and any other characters should remain unchanged. The shift value should be between 1 and 100. The function should efficiently handle large input messages with a length of up to 1 million characters.
"""

def caesar_cipher_encode(message, shift):
    encoded_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encoded_message += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encoded_message += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encoded_message += char
    return encoded_message