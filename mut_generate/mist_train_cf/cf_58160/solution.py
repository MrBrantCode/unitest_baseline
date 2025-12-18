"""
QUESTION:
Write a function `check_string(s)` that checks if a given string starts with a vowel and ends with a consonant. The function should handle case sensitivity by treating both lowercase and uppercase vowels and consonants equally, and it should ignore any non-alphabetic characters at the start or end of the string. The function should return `True` if the string meets these conditions and `False` otherwise.
"""

import re
def check_string(s):
    s = re.sub(r'[^a-zA-Z]', '', s) # Remove non-alphabetic characters
    s = s.lower() # Convert to lower case to handle case sensitivity
    if re.match(r'^[aeiou]', s) and re.search(r'[bcdfghjklmnpqrstvwxyz]$', s):
        return True
    else:
        return False