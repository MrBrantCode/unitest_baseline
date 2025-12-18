"""
QUESTION:
Create a function `char_frequency` that takes a string as input and returns a dictionary where each key is a unique character from the string and its corresponding value is the frequency of that character in the string. The function should be case sensitive and consider spaces and punctuation as characters.
"""

def char_frequency(string):
    dict = {}
    for char in string:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict