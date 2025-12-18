"""
QUESTION:
Implement a function `remove_occurrences(s, t)` that removes all occurrences of a substring `t` from a string `s`. The removal should be case-insensitive and the matching should be based on regular expressions. The substring `t` can contain special characters and regular expression metacharacters. The length of `s` is at most 10^5 and the length of `t` is at most 100. The function should have a time complexity of O(n), where n is the length of `s`.
"""

import re

def remove_occurrences(s, t):
    pattern = re.compile(re.escape(t), re.IGNORECASE)
    return re.sub(pattern, '', s)