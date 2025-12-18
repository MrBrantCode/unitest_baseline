"""
QUESTION:
Create a function `match_mythical_creatures` that identifies occurrences of the words "phoenix" and "unicorn" at the start of a paragraph, regardless of case and allowing for multiple white-spaces before, after, and in between. The function should return a list of all matches found.
"""

import re

def match_mythical_creatures(paragraph):
    pattern = r"(^[ \t]*[Pp][Hh][Oo][Ee][Nn][Ii][Xx]|[Uu][Nn][Ii][Cc][Oo][Rr][Nn])[ \t]*"
    return re.findall(pattern, paragraph, re.MULTILINE)