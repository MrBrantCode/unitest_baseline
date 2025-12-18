"""
QUESTION:
Example

Input

7
>>


Output

7
"""

import re

def calculate_min_length(n, s):
    res = 10 ** 10
    res = min(res, len(re.search('^<*', s).group()))
    res = min(res, len(re.search('>*$', s).group()))
    return n - res