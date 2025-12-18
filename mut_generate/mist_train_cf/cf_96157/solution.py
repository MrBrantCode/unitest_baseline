"""
QUESTION:
Write a function `replace_pattern` that takes four parameters: `string`, `find`, `replace`, `preceding_pattern`, and `following_pattern`. Replace all occurrences of `find` in `string` with `replace` only if `find` is not followed by `following_pattern` and preceded by `preceding_pattern`.
"""

import re

def replace_pattern(string, find, replace, preceding_pattern, following_pattern):
    pattern = f"(?<={preceding_pattern}){find}(?!{following_pattern})"
    return re.sub(pattern, replace, string)