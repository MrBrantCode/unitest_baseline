"""
QUESTION:
Implement three functions: `caesar_encrypt(text, shift)`, `caesar_decrypt(text, shift)`, and `decipher_without_key(text)`. 

The `caesar_encrypt(text, shift)` function should encrypt the given string `text` using a Caesar cipher with the provided integer `shift` key. The `caesar_decrypt(text, shift)` function should decrypt the given string `text` using a Caesar cipher with the provided integer `shift` key. The `decipher_without_key(text)` function should attempt to decipher the given string `text` without knowing the key, based on the frequency analysis of English letters. Assume the frequency of English letters is given as ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']. 

The functions should handle both lowercase and uppercase letters and preserve the case of the original letters. Non-alphabetical characters should be left unchanged.
"""

import string
from collections import Counter

# Frequency of English letters according to their commonality
english_letter_frequency = [
    'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z'
]

def caesar_encrypt(text, shift):
    """
    Encrypts the given text using a Caesar cipher with the provided shift key.
    """
    encrypted_text = ""
    for c in text:
        if c.isalpha():
            ascii_offset = ord('a') if c.islower() else ord('A')
            encrypted_text += chr((ord(c) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            encrypted_text += c
    return encrypted_text

def caesar_decrypt(text, shift):
    """
    Decrypts the given text using a Caesar cipher with the provided shift key.
    """
    return caesar_encrypt(text, -shift)

def decipher_without_key(text):
    """
    Attempts to decipher the given text without knowing the key, based on the
    frequency analysis of English letters.
    """
    # Count the frequency of each letter in the text
    text = text.lower()
    letter_counter = Counter(c for c in text if c.isalpha())

    # Sort the letter by frequency
    sorted_letters = [letter for letter, _ in letter_counter.most_common()]

    # Map the most frequent letters in the text to the most frequent letters in English
    mapping = dict(zip(sorted_letters, english_letter_frequency))

    # Apply the mapping to decipher the text
    deciphered_text = ""
    for c in text:
        if c.isalpha():
            deciphered_text += mapping.get(c, c)
        else:
            deciphered_text += c

    return deciphered_text