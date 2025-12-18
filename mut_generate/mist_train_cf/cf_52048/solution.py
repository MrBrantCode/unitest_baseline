"""
QUESTION:
Write a function `shift_letters(text)` that takes a string of letters as input and returns the string with each letter shifted one position forward in the English alphabet. If the input letter is 'z' or 'Z', it should wrap around to 'a' or 'A' respectively. Non-alphabetical characters should remain unchanged.
"""

def shift_letters(text):
    result = ""
    for i in text:
        if i.isalpha():
            if i == 'z':   # transition from z to a
                new_char = 'a'
            elif i == 'Z':   # transition from Z to A
                new_char = 'A'
            else:
                new_char = chr(ord(i) + 1)
            result += new_char
        else:
            result += i
    return result