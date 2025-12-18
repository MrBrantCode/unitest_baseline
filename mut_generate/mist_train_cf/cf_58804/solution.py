"""
QUESTION:
Implement a function named `dynamic_caesar_cipher` that takes a string `plain_text` as input and returns the encrypted string using a dynamic Caesar cipher encryption method. The shift key starts at 2 and increments by 1 after each character encryption. The function should only work with lowercase English alphabets (a-z) and assume that the input string only contains these characters. The function should not handle error checking for characters outside of the a-z range.
"""

def dynamic_caesar_cipher(plain_text):
    base = ord('a')
    cipher_text = ""
    shift = 2 

    for char in plain_text:
        index = ord(char) - base
        new_index = (index + shift) % 26
        cipher_text += chr(new_index + base)
        shift += 1 

    return cipher_text