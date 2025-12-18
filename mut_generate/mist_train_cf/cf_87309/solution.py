"""
QUESTION:
Create a function `check_substring` that takes three parameters: `string`, `substring`, `start_char`, and `end_char`. The function should return `True` if all occurrences of `substring` in `string` are surrounded by `start_char` and `end_char`, and `False` otherwise. The function should use a regular expression to achieve this.
"""

import re

def check_substring(string, substring, start_char, end_char):
    regex = r"(^|[^{}]){}{}([^{}]|$)".format(start_char, start_char, substring, end_char, end_char)
    return bool(not re.search(regex, string))