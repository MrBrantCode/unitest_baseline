"""
QUESTION:
Write a function `check_string(s)` that checks whether a given string `s` starts with a vowel and ends with a consonant, ignoring non-alphabetic characters at the start or end of the string and handling case sensitivity. The function should return the first vowel and the last consonant of the string if the conditions are met, otherwise return the first and last character of the string. If the string does not meet these conditions, throw an error.
"""

import re

def check_string(s):
    s = re.sub(r"^\W+|\W+$", "", s)
    if re.match(r'(?i)^[aeiou]', s) and re.search(r'(?i)[bcdfghjklmnpqrstvwxyz]$', s):
        start_vowel = re.search(r'(?i)[aeiou]', s).group()
        end_consonant = re.search(r'(?i)[bcdfghjklmnpqrstvwxyz](?=\W*$)', s).group()
        return start_vowel, end_consonant
    else:
        return s[0], s[-1]