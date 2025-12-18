"""
QUESTION:
Create a function named `decrypt_caesar_cipher` to decrypt a given Caesar cipher message. The function should take two parameters: `text` (the encrypted message) and `shift` (the shift value, defaulting to 3). The function should work with lowercase alphabets only and return the decrypted message.
"""

def decrypt_caesar_cipher(text, shift=3):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(shifted_alphabet, alphabet)
    return text.translate(table)