"""
QUESTION:
Write a function `extract_vowel_pattern` to extract all words from a given string that contain the letter 'a' or 'e' followed by a vowel. The function should return a list of the matched words. The words should be matched in a case-sensitive manner and the vowels are defined as 'a', 'e', 'i', 'o', and 'u'.
"""

import re

def extract_vowel_pattern(text):
    pattern = r'\b\w*[ae][aeiou]\w*\b'
    return re.findall(pattern, text)