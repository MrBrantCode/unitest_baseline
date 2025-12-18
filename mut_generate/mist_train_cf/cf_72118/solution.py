"""
QUESTION:
Write a function named `are_anagrams` that takes two strings as input, `str1` and `str2`, and returns whether they are anagrams of each other and the number of unique anagrams that can be formed from `str1`. 

The function should consider upper and lower case letters, spaces, and special characters as part of the character set, but ignore leading and trailing spaces. It should return 'Yes' and the number of unique anagrams if `str1` and `str2` are anagrams, and 'No' and 0 otherwise.
"""

from math import factorial
from collections import Counter

def are_anagrams(str1, str2):
    # Strip leading and trailing spaces
    str1 = str1.strip()
    str2 = str2.strip()
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    # Check if the sorted characters of both strings match each other
    if(sorted(str1)== sorted(str2)):
        char_freq = Counter(str1)
        numerator = factorial(len(str1))
        # Calculate denominator for number of unique anagrams using formula
        denominator = 1
        for key in char_freq:
            denominator *= factorial(char_freq[key])
        number_of_unique_anagrams = numerator//denominator  # number of unique anagrams
        return 'Yes', number_of_unique_anagrams
    else:
        return 'No', 0