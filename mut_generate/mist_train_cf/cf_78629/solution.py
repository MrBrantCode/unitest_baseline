"""
QUESTION:
Create a function called `count_upper(s)` that takes a string `s` as input and returns the number of uppercase vowels located at even indices in the string. The string `s` must be between 1 and 1000 characters in length. The function should return the count of uppercase vowels at even indices. If the length of the string is not within the given range, the function should return `False` or handle the case accordingly.
"""

def count_upper(s):
    if not 1 <= len(s) <= 1000:
        return False

    upper_vowels = 'AEIOU'
    return sum(1 for i in range(0, len(s), 2) if s[i] in upper_vowels)