"""
QUESTION:
Implement a function `replace_word(s, t, r)` that replaces all occurrences of substring `t` with `r` in string `s` only if `t` is a separate word, not part of another word. The function should take three parameters: `s` (the input string), `t` (the target word to be replaced), and `r` (the replacement word). The function should return the modified string with the replacements made.
"""

import re

def replace_word(s, t, r):
    # We add spaces around the target word to make sure it's a separate word,
    # and re.escape() to escape any special characters in 't' string
    t = re.escape(t)
    pattern = re.compile(f"\\b{t}\\b")
    
    new_s = re.sub(pattern, r, s)

    return new_s