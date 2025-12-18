"""
QUESTION:
Create a function named "cipher" that takes a string as input and returns a string where each letter is shifted 3 positions to the right (with wrap-around for 'z' and 'Z' to 'a' and 'A' respectively), numbers are shifted 3 positions to the right (with wrap-around from '9' to '0'), and non-alphabetic and non-numeric characters remain unchanged. The function must be case-sensitive and work with both uppercase and lowercase letters.
"""

def cipher(s):
    result = ''
    for char in s:
        ascii_val = ord(char)

        if 'A' <= char <= 'Z':  # uppercase letter
            result += chr((ascii_val - 65 + 3) % 26 + 65)
        elif 'a' <= char <= 'z':  # lowercase letter
            result += chr((ascii_val - 97 + 3) % 26 + 97)
        elif '0' <= char <= '9': # numbers
            result += chr((ascii_val - 48 + 3) % 10 + 48)
        else:  # non-alphabet character
            result += char

    return result