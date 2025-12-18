"""
QUESTION:
Create a function called `shannon_entropy(string)` that calculates the Shannon entropy of a given string. The string only contains lowercase letters. The function should return the calculated entropy value.
"""

import math
from collections import Counter

def shannon_entropy(string):
    frequency_list = Counter(string)
    entropy = 0.0
    len_string = len(string)
    for count in frequency_list.values():
        p_x = count / len_string
        entropy += - p_x * math.log2(p_x)
    return entropy