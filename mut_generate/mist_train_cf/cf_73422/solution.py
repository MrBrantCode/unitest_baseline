"""
QUESTION:
Write a function `encrypt(s)` that takes a string `s` as input and returns the encrypted string with the following conditions:
- The alphabet is rotated down by 4 places.
- The function maintains case sensitivity (i.e., it preserves the case of the original letters).
- The function preserves non-letter characters in the output string.
"""

def encrypt(s):
    result = ""
    for char in s:
        if char.isalpha():
            shift = 4 if char.islower() else 4
            new_char = chr(((ord(char) - 97 + shift) % 26) + 97) if char.islower() else chr(((ord(char) - 65 + shift) % 26) + 65)
            result += new_char
        else:
            result += char
    return result