"""
QUESTION:
Create a function named `is_congruent` that takes two parameters: `enc_array` (the encrypted character array) and `pat` (the preset regular expression pattern). The function should decrypt the `enc_array` by shifting every alphanumeric character back by 1 position (i.e., 'B' becomes 'A', '2' becomes '1', etc.) and '#' is considered as a decrement, then check if the decrypted string matches the given regular expression pattern. The function should return `True` if the decrypted string matches the pattern, `False` otherwise.
"""

import re

def is_congruent(enc_array, pat):
    """Decrypt enc_array by shifting every alphanumeric character back by 1 position 
    (i.e., 'B' becomes 'A', '2' becomes '1', etc.) and '#' is considered as a decrement, 
    then check if the decrypted string matches the given regular expression pattern.

    Args:
        enc_array (str): The encrypted character array.
        pat (str): The preset regular expression pattern.

    Returns:
        bool: True if the decrypted string matches the pattern, False otherwise.
    """
    dec_array = ''
    for c in enc_array:
        if c.isalpha():
            if c.islower():
                dec_array += chr((ord(c) - ord('a') - 1) % 26 + ord('a'))
            else:
                dec_array += chr((ord(c) - ord('A') - 1) % 26 + ord('A'))
        elif c.isdigit():
            dec_array += chr((ord(c) - ord('0') - 1) % 10 + ord('0'))
        elif c == '#':
            dec_array = dec_array[:-1]
        else:
            dec_array += c
    return bool(re.match(pat, dec_array))