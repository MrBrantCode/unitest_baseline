"""
QUESTION:
Write a function named `compare_string` that takes two alphanumeric strings `string1` and `string2` as input and returns a boolean value indicating whether they are permutations of each other, along with the lexicographically first character. The input strings must follow the regular expression rule /^[a-z0-9]+$/ and contain only lowercase letters and digits.
"""

import re

def compare_string(string1, string2):
    # Check if strings are alphanumeric
    pattern = r"^[a-z0-9]+$"
    if not (re.match(pattern, string1) and re.match(pattern, string2)):
        return "The strings are not alphanumeric"
    
    # Compare string lenghts
    if len(string1) != len(string2):
        return False
    
    # Sort strings
    string1 = ''.join(sorted(string1))
    string2 = ''.join(sorted(string2))
    
    if string1 == string2:
        return True, "The lexicographically first character is {}".format(string1[0])
    else:
        return False, "The lexicographically first character is {}".format(min(string1[0], string2[0]))