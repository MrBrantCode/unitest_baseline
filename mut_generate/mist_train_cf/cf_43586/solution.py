"""
QUESTION:
Write a function `count_vowels(s)` that takes a string `s` as input, filters out non-alphanumeric characters, and returns a tuple containing the total count of vowels and a dictionary with the frequency of each vowel. The function should be case-insensitive and have a time complexity of O(n), where n is the length of the string.
"""

from collections import Counter

def count_vowels(s):
    s = filter(str.isalnum, s.lower())
    count = Counter(s)
    vowels = {v: count[v] for v in 'aeiou' if v in count}
    
    return sum(vowels.values()), vowels