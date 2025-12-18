"""
QUESTION:
Create a function named `is_anagram` that takes two input strings and returns a boolean value indicating whether they are anagrams. The function should ignore case and whitespace, handle Unicode strings, and any special characters. Use a dictionary to store the frequency of each character in each string, and compare the dictionaries to determine if they are anagrams.
"""

import collections
import string

def is_anagram(str1, str2):
    # Remove whitespace and convert to lowercase
    str1 = str1.translate(str.maketrans("", "", string.whitespace)).lower()
    str2 = str2.translate(str.maketrans("", "", string.whitespace)).lower()
    # Count the frequency of each character in each string
    freq1 = collections.Counter(str1)
    freq2 = collections.Counter(str2)
    # Compare the dictionaries to determine if they are anagrams
    return freq1 == freq2