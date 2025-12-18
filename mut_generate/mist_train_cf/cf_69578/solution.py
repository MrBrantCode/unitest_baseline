"""
QUESTION:
Create a function named `char_category_counts` that takes a string as input and returns the counts of uppercase letters, lowercase letters, and special characters, as well as the frequency of each character type in the string. The function should iterate through each character in the string and categorize it as uppercase, lowercase, or special. The counts and frequency should be returned in the order of uppercase, lowercase, special, and frequency.
"""

import collections

def char_category_counts(s):
    upper, lower, special = 0, 0, 0
    freq = {'upper': collections.Counter(),
            'lower': collections.Counter(),
            'special': collections.Counter(),
           }

    for c in s:
        if c.isupper():
            upper += 1
            freq['upper'][c] += 1
        elif c.islower():
            lower += 1
            freq['lower'][c] += 1
        else:
            special += 1
            freq['special'][c] += 1

    return upper, lower, special, freq