"""
QUESTION:
Implement a function named `encode` that takes two parameters: a string `plaintext` and a string `key` containing exactly 10 characters, including both special symbols and digits. The function should return the encrypted version of `plaintext` by performing a bitwise XOR operation between each character of `plaintext` and the corresponding character in `key` (wrapping around to the start of `key` if necessary). Also, implement a corresponding `decode` function to reverse the encryption process.
"""

def encode(plaintext, key):
    """
    Encrypts the plaintext using a bitwise XOR operation with the provided key.

    Args:
    plaintext (str): The text to be encrypted.
    key (str): A string of exactly 10 characters, including both special symbols and digits.

    Returns:
    str: The encrypted version of the plaintext.
    """
    encrypted_text = "".join(
        [chr(ord(plaintext[i]) ^ ord(key[i % len(key)])) for i in range(len(plaintext))])
    return encrypted_text


def decode(encrypted_text, key):
    """
    Decrypts the encrypted text using a bitwise XOR operation with the provided key.

    Args:
    encrypted_text (str): The text to be decrypted.
    key (str): A string of exactly 10 characters, including both special symbols and digits.

    Returns:
    str: The decrypted version of the encrypted text.
    """
    decrypted_text = "".join(
        [chr(ord(encrypted_text[i]) ^ ord(key[i % len(key)])) for i in range(len(encrypted_text))])
    return decrypted_text