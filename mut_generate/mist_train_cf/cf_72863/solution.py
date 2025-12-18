"""
QUESTION:
Create a function named `anagram_check` that takes two string inputs `str1` and `str2`. The function should determine if `str1` and `str2` are anagrams, disregarding any numbers and special characters, and ignoring case. The function should be optimized for performance when dealing with longer strings.
"""

import re
from collections import Counter

def anagram_check(str1, str2):
    str1 = re.sub('[^A-Za-z]+', '', str1).lower()
    str2 = re.sub('[^A-Za-z]+', '', str2).lower()

    return Counter(str1) == Counter(str2)