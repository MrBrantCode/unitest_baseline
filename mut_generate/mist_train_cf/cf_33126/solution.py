"""
QUESTION:
Implement two functions, `vigenere_encrypt(plaintext, key)` and `vigenere_decrypt(ciphertext, key)`, to perform Vigenère cipher encryption and decryption. The functions should take a plaintext or ciphertext message and a keyword as input, and return the corresponding ciphertext or decrypted plaintext.

The Vigenère cipher encryption and decryption processes are based on the following rules: 
- Combine the message with a keyword, repeating the keyword as many times as necessary to match the length of the message. 
- Each letter in the message is shifted cyclically based on the corresponding letter in the keyword. 

Assume the message, keyword, and ciphertext will only contain uppercase and lowercase letters (no spaces or special characters). The keyword can be of any length and may contain both uppercase and lowercase letters.
"""

def vigenere_encrypt(plaintext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = ''
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = (alphabet.index(key[key_index % len(key)]) + alphabet.index(char.lower())) % 26
            if char.isupper():
                ciphertext += alphabet[shift].upper()
            else:
                ciphertext += alphabet[shift]
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = ''
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = (alphabet.index(char.lower()) - alphabet.index(key[key_index % len(key)])) % 26
            if char.isupper():
                plaintext += alphabet[shift].upper()
            else:
                plaintext += alphabet[shift]
            key_index += 1
        else:
            plaintext += char
    return plaintext