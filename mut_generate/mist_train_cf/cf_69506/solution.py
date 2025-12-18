"""
QUESTION:
Write a function `global_consonant_cluster_count` that takes a string `s` as input and returns the total number of consonant clusters in the string. The function should be case insensitive and account for consonants in various international scripts, special characters, and diacritics.
"""

import re

def global_consonant_cluster_count(s):
    pattern = r"[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]+"
    clusters = re.findall(pattern, s)
    return len(clusters)