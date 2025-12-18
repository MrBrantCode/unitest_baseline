"""
QUESTION:
Create a program with two functions, `caesar_cipher` and `caesar_decipher`, to cipher and decipher a given text using the Caesar cipher algorithm. The `caesar_cipher` function should take a text and a key as input and return the ciphered text, while the `caesar_decipher` function should take the ciphered text and the key as input and return the deciphered text. The program should handle both uppercase and lowercase letters and ignore non-alphabetic characters in the text.
"""

def caesar_cipher(text, key):
    ciphered_text = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            ciphered_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            ciphered_text += ciphered_char
        else:
            ciphered_text += char
    return ciphered_text

def caesar_decipher(ciphered_text, key):
    deciphered_text = ""
    for char in ciphered_text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            deciphered_char = chr((ord(char) - ascii_offset - key) % 26 + ascii_offset)
            deciphered_text += deciphered_char
        else:
            deciphered_text += char
    return deciphered_text