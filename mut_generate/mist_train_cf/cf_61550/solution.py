"""
QUESTION:
Create a function called `encrypt` that accepts a string `s` as input and returns an encrypted string using a shifted alphabet. The alphabet must be shifted two positions to the right, keeping case sensitivity intact and preserving non-letter elements in the final output. The function should be case-sensitive and retain non-alphabetic symbols.
"""

def encrypt(s):
    """
    Encrypts a string by shifting the alphabet two positions to the right.
    
    Parameters:
    s (str): The string to be encrypted.
    
    Returns:
    str: The encrypted string.
    """
    encrypted_string = ""
    for char in s:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + 2) % 26 + ascii_offset)
            encrypted_string += encrypted_char
        else:
            encrypted_string += char
    return encrypted_string