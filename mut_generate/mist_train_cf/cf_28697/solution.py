"""
QUESTION:
Implement a function `decrypt_text` that decrypts the given encrypted text using a simple substitution cipher, shifting each letter by a fixed number of positions down or up the alphabet. The function should take two parameters: `encrypted_text` (the text to be decrypted) and `shift` (the number of positions to shift). The function should return the decrypted text, preserving non-alphabetic characters in their original positions.
"""

def decrypt_text(encrypted_text, shift):
    decrypted = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26) + ord('a' if char.islower() else 'A'))
            decrypted += shifted_char
        else:
            decrypted += char
    return decrypted