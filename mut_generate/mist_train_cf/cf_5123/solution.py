"""
QUESTION:
Create a function `count_occurrences(words, target_word)` that counts the number of occurrences of `target_word` in an array of strings `words`. The function should be case sensitive, respect word boundaries, and ignore special characters. The input array `words` has a length between 1 and 10^6, and the `target_word` has a length between 1 and 100. The function should return an integer representing the number of occurrences of `target_word` in `words`.
"""

import re

def entrance(words, target_word):
    count = 0
    for word in words:
        # Respect word boundaries and ignore special characters
        if re.fullmatch(re.escape(target_word), word):
            count += 1
    return count