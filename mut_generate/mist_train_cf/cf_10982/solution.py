"""
QUESTION:
Write a function `vigenere_encrypt` that takes a string `plain_text` and a string `key` as input, and returns the encrypted text using the Vigenère cipher algorithm. The function should only encrypt alphabetic characters, leaving non-alphabetic characters unchanged. The key is repeated to match the length of the plain text.
"""

def vigenere_encrypt(plain_text, key):
    encrypted_text = ''
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            char = char.upper()
            char_num = ord(char) - ord('A')
            key_char = key[key_index % len(key)]
            key_num = ord(key_char.upper()) - ord('A')
            encrypted_char_num = (char_num + key_num) % 26
            encrypted_char = chr(encrypted_char_num + ord('A'))
            encrypted_text += encrypted_char if char.isupper() else encrypted_char.lower()
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text