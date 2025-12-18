"""
QUESTION:
Create a function called `transform_text` that takes two parameters: a string `text` and an integer `key`. This function should implement a substitution cipher, where each letter in the `text` is shifted by the `key` amount down the alphabet. The function should preserve the case of the letters and leave non-alphabetic characters unchanged. The output should be the encrypted text.
"""

def transform_text(text, key):
    def substitute_char(char):
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65  # ASCII values of 'a' and 'A'
            return chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
        else:
            return char  # non-alphabetic characters are not substituted

    return ''.join(substitute_char(char) for char in text)