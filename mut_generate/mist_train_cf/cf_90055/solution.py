"""
QUESTION:
Implement a function `remove_occurrences(s, t)` to remove all occurrences of a substring `t` from a string `s`, where the removal is case-insensitive and the matching is based on regular expressions. The substring `t` can contain special characters and regular expression metacharacters.

Constraints:
- The length of `s` is at most 10^5.
- The length of `t` is at most 100.
- The function should have a time complexity of O(n), where n is the length of `s`.
"""

import re

def remove_occurrences(s, t):
    pattern = re.compile(re.escape(t), re.IGNORECASE)
    return re.sub(pattern, '', s)