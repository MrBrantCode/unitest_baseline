"""
QUESTION:
Write a function `char_freq_and_positions(s)` that calculates the frequency of each distinct character in a string `s` and identifies their positions without using built-in functions. The output should be a dictionary where the keys are the characters from the string, and the values are another dictionary with two keys: 'frequency' and 'positions'. The 'frequency' key should denote the frequency of the character, and the 'positions' key should be a list holding the indices at which the character appears in the string.
"""

def char_freq_and_positions(s):
    res = {}
    for i, char in enumerate(s):
        if char not in res:
            res[char] = {'frequency': 1, 'positions': [i]}
        else:
            res[char]['frequency'] += 1
            res[char]['positions'].append(i)
    return res