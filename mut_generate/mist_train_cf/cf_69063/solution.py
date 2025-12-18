"""
QUESTION:
Implement the `caesar_cipher` function that takes two parameters, `text` and `shift`, and returns the encrypted text where each alphabetic character in `text` is transposed by `shift` positions in the alphabetical order. The function should preserve case and non-alphabetic characters. The shift should wrap around from 'z' back to 'a' or 'Z' back to 'A' if necessary.
"""

def caesar_cipher(text, shift):
    cipher_text = ""

    for char in text:
        # check if character is an uppercase letter
        if char.isupper():
            # find the position in 0-25
            pos = ord(char) - 65
            # perform the shift
            new_pos = (pos + shift) % 26
            # convert back to uppercase letter
            new_char = chr(new_pos + 65)
            # append to the cipher text
            cipher_text += new_char
        elif char.islower():
            # find the position in 0-25, for lowercase letters
            pos = ord(char) - 97
            # perform the shift
            new_pos = (pos + shift) % 26
            # convert back to lowercase letter
            new_char = chr(new_pos + 97)
            # append to the cipher text
            cipher_text += new_char
        else:
            # for any other character, just append it
            cipher_text += char

    return cipher_text