"""
QUESTION:
Create a function `caesar_cipher(text, shift)` that takes two parameters: `text` (the text to encrypt) and `shift` (the number of positions to shift the letters). Implement the Caesar cipher encryption technique, where each letter in the plaintext is shifted a certain number of positions down the alphabet, wrapping around to the beginning if necessary. Uppercase and lowercase letters should be handled separately, and any non-alphabetic characters should be left unchanged. The function should return the encrypted text.
"""

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text