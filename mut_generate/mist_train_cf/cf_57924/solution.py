"""
QUESTION:
Create a function called `encrypt` that accepts a string as input and returns an encrypted string. The encryption should be done by shifting upper case letters by 3 positions down and lower case letters by 5 positions down in the alphabet, while keeping the case sensitivity intact. Non-alphabetic characters in the input string should be preserved in the final output. The function should also handle different line endings.
"""

def encrypt(s):
    encrypted = []
    for char in s:
        if char.isupper():
            encrypted.append(chr(((ord(char) - 65 + 3) % 26) + 65))
        elif char.islower():
            encrypted.append(chr(((ord(char) - 97 + 5) % 26) + 97))
        else:
            encrypted.append(char)
    return ''.join(encrypted)