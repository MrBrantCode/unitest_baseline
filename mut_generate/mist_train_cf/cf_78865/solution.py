"""
QUESTION:
Create a function `cipher(s)` that takes a string `s` as input and returns a ciphered string. The function should shift each alphabetical character in the string three positions ahead using a rotated alphabet, handling wrapping at the ends with the modulo operator. Non-alphabetical characters should remain unchanged, and the function should preserve the case (upper and lower) of the characters. The function should work for all characters of both the lowercase and uppercase English alphabets.
"""

def cipher(s):
    result = ''
    
    for char in s:
        # preserve the non-alphabetical characters
        if not char.isalpha():
            result += char
            continue

        # shift three positions ahead, with case consideration
        shifted_char = chr((ord(char.lower()) - 97 + 3) % 26 + 97) if char.islower() else chr((ord(char.upper()) - 65 + 3) % 26 + 65)
        result += shifted_char

    return result