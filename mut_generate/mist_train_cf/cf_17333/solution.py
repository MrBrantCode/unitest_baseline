"""
QUESTION:
Implement the `caesar_cipher` function to perform Caesar Cipher encryption on a given text using a specified key. The function should take two parameters: `text` and `key`. The function must handle both uppercase and lowercase letters, shifting them by the given key while preserving non-alphabetical characters. The shift should wrap around the alphabet if necessary. The input text will only contain alphabetical characters and spaces.
"""

def caesar_cipher(text, key):
    encrypted_text = ""
    
    for char in text:
        if char.isupper():
            position = ord(char) - ord('A')
            new_position = (position + key) % 26
            new_char = chr(new_position + ord('A'))
            encrypted_text += new_char
        elif char.islower():
            position = ord(char) - ord('a')
            new_position = (position + key) % 26
            new_char = chr(new_position + ord('a'))
            encrypted_text += new_char
        else:
            encrypted_text += char
    
    return encrypted_text