"""
QUESTION:
Create a function named `caesar_cipher_encode` that takes two parameters: a string `text` and an integer `shift`. The function should encode the `text` using the Caesar cipher with the provided `shift` value. It should handle both uppercase and lowercase letters, maintain the case of the letters, and keep non-alphabetic characters unchanged. The function should also wrap around the alphabet if the `shift` value exceeds the number of letters in the alphabet.
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