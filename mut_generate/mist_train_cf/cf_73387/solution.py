"""
QUESTION:
Design a function `decipher` that takes two parameters: a string `ciphertext` and an integer `shift` between 1 and 25. The function should return the decrypted string where each alphabet character in `ciphertext` is shifted back by `shift` places in the alphabet, and non-alphabet characters remain unchanged.
"""

def decipher(ciphertext, shift):
    """
    Deciphers a string encrypted with a Caesar cipher.

    Parameters:
    ciphertext (str): The encrypted string.
    shift (int): The shift value between 1 and 25.

    Returns:
    str: The decrypted string.
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = (ord(char) - ascii_offset - shift) % 26 + ascii_offset
            plaintext += chr(decrypted_char)
        else:
            plaintext += char
    return plaintext