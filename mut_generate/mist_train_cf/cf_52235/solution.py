"""
QUESTION:
Create a function `count_upper(s)` that takes a string `s` as input and returns the number of uppercase vowel characters present at the even indices within the string.
"""

def count_upper(s):
    """Count the number of uppercase vowel characters present at the even indices within the input string"""
    upper_vowels ='AEIOU'
    return sum(1 for i in range(len(s)) if i % 2 == 0 and s[i] in upper_vowels)