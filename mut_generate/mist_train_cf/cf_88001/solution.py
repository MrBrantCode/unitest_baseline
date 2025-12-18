"""
QUESTION:
Create a Python function `caesar_encrypt` to encrypt a message using a Caesar cipher with a random shift between 1 and 26. The function should only shift the letters and leave any non-alphabetic characters unchanged. It should handle both lowercase and uppercase letters. 

Additionally, create another function `caesar_decrypt` that takes the encrypted message and the shift value as input and returns the original message. This function should also handle both lowercase and uppercase letters and leave non-alphabetic characters unchanged.
"""

def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message