"""
QUESTION:
Create a function named `encrypt` that takes a string input and returns the encrypted string using the ROT13 cipher. The function should only produce output with uppercase letters and ignore non-alphabetic characters. Additionally, the input string must be at least 10 characters long; otherwise, the function should return an error message.
"""

def encrypt(text):
    if len(text) < 10:
        return "Error: Input string must be at least 10 characters long."
    cipher = ""
    for char in text:
        if not char.isalpha():
            # Ignore non-alphabetic characters
            cipher += char
        else:
            # Shift the character by 13 places
            shifted = chr((ord(char.upper()) - 65 + 13) % 26 + 65)
            cipher += shifted
    return cipher