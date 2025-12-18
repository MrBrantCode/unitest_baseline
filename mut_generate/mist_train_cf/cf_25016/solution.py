"""
QUESTION:
Implement a function called `encrypt_string` that takes a string input and encrypts it using a substitution cipher. The function should return the encrypted string.
"""

def encrypt_string(input_str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    cipher = 'nopqrstuvwxyzabcdefghijklm'
    encrypted_str = ''
    for char in input_str:
        if char.isalpha():
            if char.islower():
                index = alphabet.index(char)
                encrypted_str += cipher[index]
            else:
                index = alphabet.index(char.lower())
                encrypted_str += cipher[index].upper()
        else:
            encrypted_str += char
    return encrypted_str