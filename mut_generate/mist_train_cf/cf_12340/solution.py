"""
QUESTION:
Write a function `modified_caesar_cipher` that takes two parameters: a string `text` and an integer `shift`. The function should reverse the order of the letters in `text`, then shift each letter by the given `shift` amount (which is the ASCII value of the previous letter in the alphabet). The function should return the encrypted text as a string. The input `text` is assumed to contain only lowercase letters.
"""

def modified_caesar_cipher(text, shift):
    reversed_text = text[::-1]  # Reverse the order of the letters

    encrypted_text = ""
    for letter in reversed_text:
        ascii_value = ord(letter) + shift  # Shift each letter by the given amount
        encrypted_text += chr(ascii_value)

    return encrypted_text