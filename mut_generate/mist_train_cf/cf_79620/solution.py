"""
QUESTION:
Write a function named `check_vowels` that takes a string as input and returns the total count of distinct vowels if the string contains at least two distinct vowels. The function should be case-insensitive. If the string contains less than two distinct vowels, return False.
"""

import re
from collections import Counter

def check_vowels(string):
    vowels = re.findall('[aeiou]', string.lower())
    vowel_counter = Counter(vowels)
    
    distinct_vowels = {k: v for k,v in vowel_counter.items() if v >= 1}
    
    if len(distinct_vowels) < 2:
        return False
    else:
        return sum(distinct_vowels.values())