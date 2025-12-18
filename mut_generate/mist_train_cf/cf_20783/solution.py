"""
QUESTION:
Create a function named `decrypt_string` that takes two parameters: `encrypted_string` and `encryption_alphabet`. The function should decrypt the `encrypted_string` using the `encryption_alphabet`, which is a 26-character string of lowercase letters representing a substitution cipher. The function should return the decrypted string. The `encrypted_string` will only contain lowercase letters and the `encryption_alphabet` will always be a valid string of 26 lowercase letters.
"""

def decrypt_string(encrypted_string, encryption_alphabet):
    decryption_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_string = ""
    for char in encrypted_string:
        if char.isalpha():
            index = encryption_alphabet.index(char)
            decrypted_string += decryption_alphabet[index]
        else:
            decrypted_string += char
    return decrypted_string