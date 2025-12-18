"""
QUESTION:
Create a function `multi_replace(s, t, r)` that replaces all occurrences of strings in list `t` with corresponding strings in list `r` within string `s`. The function must handle overlapping and embedded string matches and perform in constant space.
"""

import re

def multi_replace(s, t, r):
    replace_dict = dict(zip(t, r))
    pattern = '|'.join(map(re.escape, replace_dict.keys()))
    return re.sub(pattern, lambda x: replace_dict[x.group()], s)