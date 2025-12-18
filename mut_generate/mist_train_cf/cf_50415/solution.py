"""
QUESTION:
Create a function called `shift_letters(s)` that takes a string `s` as input and returns a new string where each alphabetic character is replaced with the subsequent letter in the English alphabetical order, wrapping around to 'a' or 'A' when 'z' or 'Z' is encountered, while non-alphabetic characters remain unchanged.
"""

def shift_letters(s):
    result = ""
    for c in s:
        if c.isalpha():  
            if c.lower() == 'z':  
                result += 'a' if c.islower() else 'A'
            else:  
                result += chr(ord(c) + 1)
        else:  
            result += c

    return result