"""
QUESTION:
Implement a function `caesar_cipher_encrypt(text, key)` that encrypts the input text using the Caesar Cipher method with a given key. The function should shift all uppercase and lowercase letters by the specified key, while keeping punctuation and spaces unchanged. The shift should wrap around the alphabet if necessary.
"""

def caesar_cipher_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine the appropriate shift based on uppercase or lowercase
            if char.isupper():
                shift = ord('A')
            else:
                shift = ord('a')
            # Encrypt the character
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            # Append punctuation and spaces as is
            encrypted_text += char
    return encrypted_text