"""
QUESTION:
Create a function `count_upper` that takes a string `s` as input and returns the count of uppercase vowels found exclusively at even indices in the string. The function should consider 'A', 'E', 'I', 'O', 'U' as the only vowels.
"""

def count_upper(s):
    upper_vowels = 'AEIOU'
    return sum(1 for i in range(len(s)) if i % 2 == 0 and s[i] in upper_vowels)