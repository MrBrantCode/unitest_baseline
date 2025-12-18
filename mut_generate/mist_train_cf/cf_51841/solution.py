"""
QUESTION:
Create a function `predict_next_char(text)` that takes a string of characters as input and returns the next alphabetical character following the last character in the string. The function should wrap around to 'a' if the last character is 'z' and handle cases where the last character is not alphabetical.
"""

def predict_next_char(text):
    last_char = text[-1].lower()
    if last_char == 'z':
        return 'a'
    elif not last_char.isalpha():
        return 'a' # return 'a' if the last character is not alphabetical
    else:
        return chr(ord(last_char) + 1)