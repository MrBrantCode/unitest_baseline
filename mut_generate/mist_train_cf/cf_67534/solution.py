"""
QUESTION:
Create a function `char_frequency` that takes a string as input and returns a dictionary where each key is a unique character from the string and the corresponding value is the frequency of its occurrence. The function should handle any type of character in the input string.
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