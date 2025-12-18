"""
QUESTION:
# Introduction 

A grille cipher was a technique for encrypting a plaintext by writing it onto a sheet of paper through a pierced sheet (of paper or cardboard or similar). The earliest known description is due to the polymath Girolamo Cardano in 1550. His proposal was for a rectangular stencil allowing single letters, syllables, or words to be written, then later read, through its various apertures. The written fragments of the plaintext could be further disguised by filling the gaps between the fragments with anodyne words or letters. This variant is also an example of steganography, as are many of the grille ciphers. 
Wikipedia Link 

![Tangiers1](https://upload.wikimedia.org/wikipedia/commons/8/8a/Tangiers1.png)
![Tangiers2](https://upload.wikimedia.org/wikipedia/commons/b/b9/Tangiers2.png)

# Task

Write a function that accepts two inputs: `message` and `code` and returns hidden message decrypted from `message` using the `code`.   
The `code` is a nonnegative integer and it decrypts in binary the `message`.
"""

def decrypt_grille_cipher(message, code):
    """
    Decrypts the given message using the grille cipher technique with the provided code.

    Parameters:
    - message (str): The encrypted message to be decrypted.
    - code (int): A nonnegative integer used to decrypt the message.

    Returns:
    - str: The decrypted message.
    """
    return ''.join((message[-1 - i] for (i, c) in enumerate(bin(code)[::-1]) if c == '1' and i < len(message)))[::-1]