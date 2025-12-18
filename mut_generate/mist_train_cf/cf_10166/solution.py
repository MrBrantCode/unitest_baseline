"""
QUESTION:
Create a custom encryption algorithm to encode a string of characters without relying on built-in encryption functions or libraries. The algorithm should include a decryption function to decode the encoded string back to its original form. The algorithm should handle uppercase and lowercase letters and non-alphabet characters. The functions should take two parameters: the string to be encrypted/decrypted and the shift value. The functions should return the encrypted/decrypted string.
"""

def caesar_cipher(string, shift):
    result = ""
    for char in string:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt_caesar_cipher(string, shift):
    decrypted = ""
    for char in string:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            decrypted += char
    return decrypted