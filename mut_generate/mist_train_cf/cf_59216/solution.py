"""
QUESTION:
Write a function `min_operations(s1, s2)` that calculates the minimum number of operations (character changes) needed to convert string `s1` into an anagram of string `s2`. The function should handle strings of different lengths and characters, including non-alphabetic characters and null strings.
"""

from collections import Counter

def min_operations(s1, s2):
    counter_s1 = Counter(s1)
    counter_s2 = Counter(s2)
    for key in counter_s2.keys():
        counter_s1[key] -= min(counter_s1[key], counter_s2[key])
    return sum(counter_s1.values())