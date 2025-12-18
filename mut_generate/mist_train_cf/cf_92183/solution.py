"""
QUESTION:
Implement a function named `caesar_cipher` that takes two parameters: a string to be encrypted and an integer shift value between 1 and 25 (inclusive). The function should apply the Caesar Cipher encryption to the input string, handling both uppercase and lowercase letters while leaving non-alphabetic characters unchanged. The function should return the encrypted string with a time complexity of O(n), where n is the length of the input string.
"""

def caesar_cipher(string, shift):
    shift = shift % 26
    encrypted_string = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_string += encrypted_char
    return encrypted_string