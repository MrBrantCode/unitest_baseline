"""
QUESTION:
Create a function `caesar_cipher(s, offset)` that encodes a given string `s` by shifting each alphabetic character by a given integer `offset` while preserving non-alphabetic characters and the case of the original letters, and wrapping around the alphabet if necessary.
"""

def caesar_cipher(s, offset):
    result = ""
    for v in s:
        if v.isalpha():
            stay_in_alphabet = ord(v) + offset 
            if v.isupper():
                new_char = chr(stay_in_alphabet) if stay_in_alphabet <= ord('Z') else chr(stay_in_alphabet - 26)
            else:
                new_char = chr(stay_in_alphabet) if stay_in_alphabet <= ord('z') else chr(stay_in_alphabet - 26)
            result += new_char
        else:
            result += v
    return result