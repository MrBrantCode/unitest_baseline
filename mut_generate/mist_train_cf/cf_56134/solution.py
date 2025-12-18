"""
QUESTION:
Implement a function named `caesar_cipher` that takes two parameters, `text` and `shift`, and returns the encrypted text using the Caesar cipher algorithm. The function should correctly handle uppercase and lowercase letters, wrapping from Z to A, and non-alphabetical characters. The shift should be applied modulo 26 to support shifts greater than the length of the alphabet.
"""

def caesar_cipher(text, shift):
  
    cipher_text = ""
    shift %= 26 

    for character in text:
        if character.isalpha():
            ascii_offset = ord('a') if character.islower() else ord('A')
            cipher_character = chr((ord(character) - ascii_offset + shift) % 26 + ascii_offset)
            cipher_text += cipher_character
        else:
            cipher_text += character
  
    return cipher_text