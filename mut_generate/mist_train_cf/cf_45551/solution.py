"""
QUESTION:
Construct a function `construct_regexp(begin_str, any_str, end_str)` that returns a regular expression pattern. The pattern should match any string that starts with `begin_str`, contains `any_str` anywhere, and ends with `end_str`. The function should properly handle special characters in the input strings.
"""

import re

def construct_regexp(begin_str, any_str, end_str):
    return re.compile(r"^" + re.escape(begin_str) + r".*" + re.escape(any_str) + r".*" + re.escape(end_str) + r"$")