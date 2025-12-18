"""
QUESTION:
Write a function `char_frequency(str1)` that takes a string `str1` as input and returns a dictionary where the keys are unique characters in the string and the values are their corresponding frequency counts.
"""

def char_frequency(str1):
    dict = {}
    for char in str1:
        keys = dict.keys()
        if char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict