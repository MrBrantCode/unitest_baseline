"""
QUESTION:
Implement a function `caesar_cipher_encode(text, shift)` that encodes a given text string using the Caesar cipher with a variable shift. The function should handle both uppercase and lowercase letters, maintain their original case, and wrap around the alphabet if necessary. Non-alphabetic characters should remain unchanged and maintain their original positions in the encoded string.
"""

def caesar_cipher_encode(text, shift):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encoded_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encoded_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encoded_char = char
        encoded_text += encoded_char
    return encoded_text