"""
QUESTION:
Create a function named `rot13` that takes a string message as input and returns the encrypted string using the ROT13 cipher. The function should replace each alphabetic character with the letter 13 places down the alphabet, preserving the case of the original character, and leave non-alphabetic characters unchanged.
"""

def rot13(message):
    encrypted = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted += chr((ord(char) - 97 + 13) % 26 + 97)
            else:
                encrypted += chr((ord(char) - 65 + 13) % 26 + 65)
        else:
            encrypted += char
    return encrypted