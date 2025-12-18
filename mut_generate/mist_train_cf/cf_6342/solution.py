"""
QUESTION:
Create a function named `caesar_cipher(text, shift)` that encodes a given text string using the Caesar cipher with a variable shift. The function should handle uppercase and lowercase letters, special characters (including punctuation marks), and numbers, maintaining their original positions in the encoded string. It should also wrap around the alphabet if the shift value exceeds the number of letters. The implementation must not use built-in string manipulation functions or methods and should be optimized for efficiency and readability.
"""

def caesar_cipher(text, shift):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for char in text:
        if char in alphabet:
            is_upper = char.isupper()
            index = alphabet.index(char.lower())
            new_index = (index + shift) % len(alphabet)
            new_char = alphabet[new_index]
            if is_upper:
                result += new_char.upper()
            else:
                result += new_char
        else:
            result += char

    return result