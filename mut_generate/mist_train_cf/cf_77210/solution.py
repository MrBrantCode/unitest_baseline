"""
QUESTION:
Create a function called `char_frequency` that takes a string as input and returns a dictionary where keys are the distinct characters in the string (including upper-case and lower-case alphabets, digits, and special characters) and values are their respective frequency counts. The function should ignore white spaces in the string.
"""

def char_frequency(s):
    dict = {}
    for n in s:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        elif n != ' ':  # ignore white spaces
            dict[n] = 1
    return dict