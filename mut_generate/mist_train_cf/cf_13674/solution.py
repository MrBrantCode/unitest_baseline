"""
QUESTION:
Create a function `encrypt(value)` that takes a string `value` and returns the encrypted string using a custom encryption algorithm. The function should shift each character in the string by one ASCII value.
"""

def encrypt(value):
    """
    Encrypts a string by shifting each character by one ASCII value.

    Args:
        value (str): The input string to be encrypted.

    Returns:
        str: The encrypted string.
    """
    encrypted_value = ""
    for char in value:
        encrypted_value += chr(ord(char) + 1)  # Shifts each character by 1 ASCII value
    return encrypted_value