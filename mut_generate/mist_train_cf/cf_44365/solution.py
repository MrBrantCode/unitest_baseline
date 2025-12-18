"""
QUESTION:
Implement a function `caesar_cipher_encrypt` that encrypts a given UTF-8 text using a Caesar Cipher algorithm. The function should take two parameters: `text` (the input string to be encrypted) and `shift` (the number of positions to shift the characters). The function should return the encrypted string. The function should handle both uppercase and lowercase letters, wrapping around the alphabet if necessary, and should not modify non-alphabetic characters.
"""

def caesar_cipher_encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += chr((ord(char) - 97 + shift) % 26 + 97)

    return result