"""
QUESTION:
Write a function named `decrypt_caesar_cipher` to decrypt a given cipher text using the Caesar cipher with a shift of 3 positions. The function should take a string `cipher_text` as input and return the decrypted text. The shift should wrap around the alphabet if necessary. The function should only work with lowercase English letters.
"""

def decrypt_caesar_cipher(cipher_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    for char in cipher_text:
        i = (alphabet.index(char) - 3) % 26
        output += alphabet[i]
    return output