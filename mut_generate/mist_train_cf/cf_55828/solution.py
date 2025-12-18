"""
QUESTION:
Design a function `char_frequency(str1)` that generates a dictionary with the unique alphabetic characters from a given string as keys and their respective occurrence frequency as values, ignoring non-alphabetic characters such as spaces, punctuation, and numbers.
"""

def char_frequency(str1):
    dict1 = {}
    str1 = ''.join(e for e in str1 if e.isalpha()) 
    for n in str1:
        keys = dict1.keys()
        if n in keys:
            dict1[n] += 1
        else:
            dict1[n] = 1
    return dict1