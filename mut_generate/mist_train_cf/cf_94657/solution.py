"""
QUESTION:
Write a function called `caesar_cipher` that takes a string `text` and an integer `key` as input and returns the encrypted text using the Caesar Cipher technique. The input text contains only alphabetical characters and spaces. The function should shift each letter in the text by the given key positions down the alphabet while keeping non-alphabetical characters unchanged.
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