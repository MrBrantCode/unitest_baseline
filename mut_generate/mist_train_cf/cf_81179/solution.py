"""
QUESTION:
Create a function named `transposition_cipher` that takes a string `text` and an integer `key` as input. The function should implement a simple transposition cipher to rearrange the characters in the input `text` based on the provided `key`. The function should return the encrypted text as a string. The length of the input `text` is a multiple of the `key`.
"""

def transposition_cipher(text, key):
    cipher = [''] * key

    for col in range(key):
        position = col
        while position < len(text):
            cipher[col] += text[position]
            position += key
            
    return ''.join(cipher)