"""
QUESTION:
Write a function `decrypt_string` that takes two arguments: `encrypted_string` and `encryption_alphabet`. The function should decrypt the `encrypted_string` using the `encryption_alphabet`, where each character in the `encrypted_string` is replaced with a corresponding character based on the index in the `encryption_alphabet`. The `encryption_alphabet` will always be a valid string of 26 lowercase letters, and the `encrypted_string` will only contain lowercase letters. The function should return the decrypted string.
"""

def decrypt_string(encrypted_string, encryption_alphabet):
    decrypted_string = ""
    for char in encrypted_string:
        index = encryption_alphabet.index(char)
        decrypted_string += chr(index + 97)
    return decrypted_string