"""
QUESTION:
Write a function `next_alphabet(txt)` that returns the consecutive alphabetical character following the last character of the input string `txt`. If the last character is 'z' or 'Z', wrap around to 'a' or 'A' respectively. If the input string is empty or the last character is not an alphabet, return an error message.
"""

def next_alphabet(txt):
    if not txt:    # In case of empty string
        return 'Error: Input string is empty.'
    if not txt[-1].isalpha():  # In case of non-alphabetical characters
        return 'Error: Last character is not an alphabet.'
    elif txt[-1] == 'z':
        return 'a'
    elif txt[-1] == 'Z':
        return 'A'
    else:
        return chr(ord(txt[-1]) + 1)