"""
QUESTION:
Create a function `char_frequency(string)` that takes a string of any length as input and returns a dictionary where the keys are the unique characters in the string and the values are their corresponding frequencies. The function should be case sensitive, handle special characters and numbers, and consider whitespace as a character.
"""

def char_frequency(string):
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict