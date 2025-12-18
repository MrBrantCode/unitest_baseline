"""
QUESTION:
Implement a function named `caesar_cipher` that encodes a given text string using the Caesar cipher with a variable shift. The function should handle special characters, including punctuation marks, and maintain their original positions in the encoded string. It should also handle both uppercase and lowercase letters correctly and wrap around the alphabet if the shift value exceeds the number of letters. The function should not use built-in string manipulation functions or methods, and it should be optimized for efficiency and readability.
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