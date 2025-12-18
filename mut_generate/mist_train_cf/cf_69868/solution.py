"""
QUESTION:
Create a function `match_hex_vowel` that takes a string as input and returns `True` if the string matches a hexadecimal quantity followed by a lowercase English vowel, and `False` otherwise. The function should use a regular expression pattern that matches one or more hexadecimal digits followed by a single lowercase English vowel (a, e, i, o, or u), with word boundaries to avoid partial word matches.
"""

import re

def match_hex_vowel(string):
    # The regexp starts with \b to match the start of a word
    # Following that, [0-9A-Fa-f]+ matches one or more hexadecimal digits
    # After that, [aeiou] matches a single lowercase English vowel
    # Finally, \b matches the end of a word to avoid partial word matches 
    pattern = r'\b[0-9A-Fa-f]+[aeiou]\b'
    return re.match(pattern, string) is not None