"""
QUESTION:
Write a function `caesar_cipher(text, keys, exclude_chars=None)` that encrypts the input `text` using the Caesar Cipher algorithm with multiple keys. The function should handle both uppercase and lowercase letters, punctuation, and spaces without altering them. The keys can be either positive or negative integers. If a key is a prime number, apply a different encryption algorithm. The function should also support an optional parameter `exclude_chars` to specify a custom list of characters that should not be encrypted.
"""

import string

def caesar_cipher(text, keys, exclude_chars=None):
    result = []
    exclude_chars = exclude_chars or []
    
    for key in keys:
        if key in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:  
            encrypted_text = ""
            for char in text:
                if char in exclude_chars:
                    encrypted_text += char
                elif char.isalpha():
                    if char.isupper():
                        encrypted_char = chr((ord(char) - 65 + key) % 26 + 65)
                    else:
                        encrypted_char = chr((ord(char) - 97 + key) % 26 + 97)
                    encrypted_text += encrypted_char
                else:
                    encrypted_text += char
            result.append(encrypted_text)
        else:
            alphabet = string.ascii_letters
            shifted_alphabet = alphabet[key:] + alphabet[:key]
            table = str.maketrans(alphabet, shifted_alphabet)
            result.append(text.translate(table))
    
    return result