"""
QUESTION:
Create a function called `get_shortest_without_vowels` that takes three distinct string variables as input. The function should remove all vowel characters from each string and return the shortest resulting string. The comparison should be case-insensitive when removing vowels.
"""

def get_shortest_without_vowels(s1, s2, s3):
    vowels = 'aeiou'
    s1_without_vowels = ''.join([c for c in s1 if c.lower() not in vowels])
    s2_without_vowels = ''.join([c for c in s2 if c.lower() not in vowels])
    s3_without_vowels = ''.join([c for c in s3 if c.lower() not in vowels])

    return min(s1_without_vowels, s2_without_vowels, s3_without_vowels, key=len)