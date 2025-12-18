"""
QUESTION:
Write a function `char_frequency` that takes a string `str1` as input and returns a dictionary where the keys are the unique characters in the string and the values are their corresponding frequencies. The function should count spaces as characters.
"""

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict