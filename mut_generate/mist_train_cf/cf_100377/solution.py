"""
QUESTION:
Write a function `to_unicode_code_points(sentence, encoding='utf-8', min_value=0, max_value=sys.maxunicode)` that converts a given sentence into an array of Unicode code points. The function should handle multi-byte characters, include punctuation marks, and ensure that the resulting Unicode code points are within a certain range of values and the encoding is compatible with different platforms and databases.
"""

import sys

def to_unicode_code_points(sentence, encoding='utf-8', min_value=0, max_value=sys.maxunicode):
    code_points = []
    encoded_sentence = sentence.encode(encoding)
    for b in encoded_sentence:
        if min_value <= b <= max_value:
            code_points.append(b)
    return code_points