"""
QUESTION:
Create a function named `consonant_shift(s)` that takes a string `s` as input and returns a modified version of the string where all consonant characters are shifted to the next consonant in alphabetical order (wrapping around from 'z' to 'b' and from 'Z' to 'B' for uppercase letters). Non-consonant characters should remain unchanged.
"""

def consonant_shift(s):
    result = ""
    for letter in s:
        if letter.isalpha() and letter.lower() not in "aeiou":
            if letter.lower() == 'z':
                result += 'b' if letter.islower() else 'B'
            else:
                result += chr(ord(letter) + 1)
        else:
            result += letter
    return result