"""
QUESTION:
Implement a function named `reverse_string` that takes a Unicode string as input and returns the reversed string. The function should correctly handle surrogate pairs, which are Unicode characters that require 32 bits to be represented and are represented using a pair of 16-bit numbers.
"""

import re

def reverse_string(s):
    unicode_chars = re.findall(r'[\uD800-\uDBFF][\uDC00-\uDFFF]|[^\uD800-\uDFFF]', s)
    reversed_s = ''.join(unicode_chars[::-1])
    return reversed_s