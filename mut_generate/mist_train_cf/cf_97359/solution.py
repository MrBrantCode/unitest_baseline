"""
QUESTION:
Create a function `characters_appear_in_order(string1, string2)` that checks if the alphanumeric characters in `string1` appear in order and consecutively in `string2`, considering a case-insensitive comparison and unique characters in `string2`.
"""

import re

def characters_appear_in_order(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    string1 = re.sub(r'\W+', '', string1)
    string2 = re.sub(r'\W+', '', string2)

    i = 0

    for char in string2:
        if char == string1[i]:
            i += 1

            if i == len(string1):
                return True

    return False