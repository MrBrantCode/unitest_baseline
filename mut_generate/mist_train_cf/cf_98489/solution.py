"""
QUESTION:
Implement a function named `encrypt` that takes two parameters: `text` and `s`. The `text` parameter is a string to be encrypted, and the `s` parameter is an integer representing the number of positions to shift each letter down the alphabet. The function should return the encrypted string using the Caesar cipher method, shifting both uppercase and lowercase letters while preserving their original case.
"""

def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result