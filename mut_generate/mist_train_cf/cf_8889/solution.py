"""
QUESTION:
Create a function `remove_spaces_and_punctuation` that takes a string as input, removes all non-alphanumeric characters (including spaces and punctuation marks), and returns the modified string. The function should preserve the order of alphanumeric characters and handle both uppercase and lowercase letters, as well as digits.
"""

import re

def remove_spaces_and_punctuation(s):
    return re.sub('[^a-zA-Z0-9]', '', s)