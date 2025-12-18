"""
QUESTION:
Write a function named `generate_all_strings` that generates all possible binary strings of a given length `n` without any consecutive '1's. The function should be able to handle arbitrary binary string lengths and must use memoization for efficiency.
"""

from functools import lru_cache

@lru_cache(maxsize = 1000)
def generate_all_strings(n):
    if n == 0 : return []
    if n == 1 : return ["0", "1"]
    
    result = []
    for str in generate_all_strings(n - 1):
        if not ('11' in (str + '0')):
            result.append(str + '0')
        if not ('11' in (str + '1')):
            result.append(str + '1')

    return result