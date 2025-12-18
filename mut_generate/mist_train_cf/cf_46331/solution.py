"""
QUESTION:
Write a function `count_reverse_pairs(lst)` that takes a list of strings as input and returns the number of reversed string pairs. The function should ignore special characters, numerals, case sensitivity, and spaces when counting the reversed string pairs.
"""

import re

def count_reverse_pairs(lst):
    count = 0
    for i in range(len(lst)):
        s1 = re.sub('[^a-zA-Z]', '', lst[i]).lower().replace(" ", "")
        for j in range(i+1, len(lst)):
            s2 = re.sub('[^a-zA-Z]', '', lst[j]).lower().replace(" ", "")
            if s1 == s2[::-1]:
                count += 1
    return count