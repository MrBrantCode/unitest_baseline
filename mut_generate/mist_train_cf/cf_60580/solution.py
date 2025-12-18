"""
QUESTION:
Create a function named `Caesar_Cipher` that takes a string `text` and an integer `shift` as inputs, and returns the encrypted text using the Caesar Cipher encryption method. The function should handle non-alphabet characters by leaving them unchanged, and it should account for the circular nature of alphabets by wrapping around the ASCII ranges for lowercase and uppercase letters.
"""

def Caesar_Cipher(text, shift):
    encrypted_text = ""
    for c in text:
        if not c.isalpha():
            encrypted_text += c
        elif c.isupper():
            encrypted_text += chr((ord(c) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += chr((ord(c) - 97 + shift) % 26 + 97)
    return encrypted_text