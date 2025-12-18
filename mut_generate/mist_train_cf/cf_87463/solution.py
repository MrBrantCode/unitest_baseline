"""
QUESTION:
Write a function called `caesar_cipher` that takes two parameters: `text` (a string containing alphabetical characters and spaces) and `key` (a positive integer less than or equal to 26). The function should perform the Caesar Cipher encryption technique on the text using the given key and return the encrypted text. The technique involves shifting each letter in the text by the key number of positions down the alphabet, wrapping around the alphabet if necessary, and leaving non-alphabetical characters unchanged.
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