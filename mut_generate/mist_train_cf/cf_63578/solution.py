"""
QUESTION:
Implement a Caesar cipher encryption function, `encrypt(text, shift)`, that takes two parameters: `text` (the string to be encrypted) and `shift` (the number of positions each character in the plaintext should be shifted down the alphabet). The function should encrypt both uppercase and lowercase characters, preserving their case, and handle wrap-around from 'z' to 'a' and 'Z' to 'A'.
"""

def encrypt(text, shift):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]
   
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + shift-65) % 26 + 65)
  
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result