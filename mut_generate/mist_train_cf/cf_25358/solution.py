"""
QUESTION:
Write a function named `caesar_encode` that takes two parameters: a string `s` and an integer `k`. The function should implement a Caesar cipher to shift each lowercase letter in the string `s` by `k` places in the alphabet, wrapping around to the beginning if necessary, and return the encoded string. The function should only handle lowercase letters and should not modify any non-alphabetic characters.
"""

def caesar_encode(s, k):
    """
    Encode a string using Caesar cipher.

    Parameters:
    s (str): The input string to be encoded.
    k (int): The shift value for the Caesar cipher.

    Returns:
    str: The encoded string.
    """
    encoded_str = ""
    for char in s:
        if char.isalpha() and char.islower():
            # Shift each character with the given key
            enc = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
            encoded_str += enc
        else:
            encoded_str += char
    return encoded_str