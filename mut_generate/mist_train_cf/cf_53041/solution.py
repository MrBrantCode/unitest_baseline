"""
QUESTION:
Create a function `encrypt(text, key)` that encrypts a given message using a Caesar cipher with the specified key. The function should shift each letter in the message by the value of the key, while leaving non-alphabet characters unchanged. The shift should wrap around the alphabet if necessary.
"""

def caesar_encrypt(text, key):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - 65 + key) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - 97 + key) % 26 + 97)
        
        # For punctuation and spaces
        else:
            result += char

    return result