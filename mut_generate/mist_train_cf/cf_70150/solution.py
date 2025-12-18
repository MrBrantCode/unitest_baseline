"""
QUESTION:
Implement a Caesar cipher algorithm to encrypt and decrypt historical document text. Create two functions, `caesar_encrypt` and `caesar_decrypt`, that take a string `text` and an integer `shift` as parameters. The `caesar_encrypt` function should return the encrypted text, and the `caesar_decrypt` function should return the decrypted text. The functions should handle both lowercase and uppercase characters, and the shift should be applied to the alphabet. The solution should be implemented in Python and should not use any external libraries for encryption.
"""

import string

def caesar_encrypt(text, shift):
    """
    A function to encrypt a message using a Caesar cipher
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    
    lower_table = str.maketrans(lower, lower[shift:] + lower[:shift])
    upper_table = str.maketrans(upper, upper[shift:] + upper[:shift])
    
    encrypted_text = text.translate(lower_table).translate(upper_table)
    
    return encrypted_text


def caesar_decrypt(text, shift):
    """
    A function to decrypt a message using a Caesar cipher
    """
    return caesar_encrypt(text, -shift)