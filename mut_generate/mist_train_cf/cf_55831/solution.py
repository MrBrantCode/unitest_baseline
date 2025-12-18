"""
QUESTION:
Implement a function named `caesar_decipher` that takes two parameters: `string` and `shift`, and returns the decoded string by applying a Caesar cipher with the specified shift. The function should only shift letters, preserve case, and wrap around the alphabet from 'z' to 'a' and 'Z' to 'A'.
"""

def caesar_decipher(string, shift):
    """
    Deciphers a caesar cipher of a string using the specified shift.
    """
    def shift_letter(letter, shift):
        """
        Shifts a letter by "shift" positions. 
        Wraps around the alphabet from z->a and Z->A.
        """
        ascii_offset = ord('a') if letter.islower() else ord('A')
        new_letter_code = (ord(letter) - ascii_offset + shift) % 26 + ascii_offset
        return chr(new_letter_code)

    # To decipher, we simply apply a negative shift.
    return ''.join(shift_letter(letter, -shift) if letter.isalpha() else letter for letter in string)