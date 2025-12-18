"""
QUESTION:
Design a function named `char_frequency` that takes a string as input and returns a dictionary where each unique character in the string is a key and its corresponding value is the frequency of occurrence of that character in the string.
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