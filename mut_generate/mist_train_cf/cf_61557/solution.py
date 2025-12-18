"""
QUESTION:
Create a function called `has_z_followed_by_two_ys` that takes a string as an argument and returns `True` if the string contains a 'z' followed by two or more 'y's, and `False` otherwise.
"""

import re

def has_z_followed_by_two_ys(string):
    return re.search(r'zy{2,}', string) is not None