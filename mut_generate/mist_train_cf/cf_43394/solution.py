"""
QUESTION:
Create a function `caesar_encrypt(text, shift)` that takes two parameters: `text` and `shift`, where `text` is the input string to be encrypted and `shift` is the number of positions each letter in the `text` should be shifted down the alphabet. The function should implement the Caesar cipher encryption technique, replacing each letter with a letter a fixed number of positions down the alphabet, and leaving non-alphabetic characters unchanged.
"""

def caesar_encrypt(text, shift):
    result = ""

    # iterate over each character
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)

        # Encrypt lowercase characters
        elif (char.islower()):
            result += chr((ord(char) + shift-97) % 26 + 97)

        # Leave all other characters as they are
        else:
            result += char

    return result