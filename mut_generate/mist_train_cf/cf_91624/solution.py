"""
QUESTION:
Write a function `vigenere_encrypt` that takes a plain text string and a key string as input and returns the encrypted text string using the Vigenère cipher algorithm. The function should encrypt alphabetic characters in the plain text while non-alphabetic characters should be appended to the encrypted text without any encryption. The function should handle both uppercase and lowercase alphabetic characters in the plain text and key.
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
            if char.islower():
                encrypted_char = chr(encrypted_char_num + ord('a'))
            else:
                encrypted_char = chr(encrypted_char_num + ord('A'))
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text