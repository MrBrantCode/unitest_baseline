"""
QUESTION:
Write a function `compare_strings` that takes two parameters, `string1` and `string2`, and returns `True` if the two strings have the same number of characters and the number of vowels in `string1` is equal to the number of consonants in `string2`. A consonant is defined as a letter that is not a vowel (a, e, i, o, u). The comparison should be case-insensitive.
"""

def compare_strings(string1, string2):
    # Count the number of characters in each string
    len1 = len(string1)
    len2 = len(string2)
    
    # Check if the number of characters is equal
    if len1 != len2:
        return False
    
    # Count the number of vowels and consonants in each string
    vowels1 = sum(1 for char in string1 if char.lower() in 'aeiou')
    consonants2 = sum(1 for char in string2 if char.lower() not in 'aeiou')
    
    # Check if the number of vowels in string1 is equal to the number of consonants in string2
    return vowels1 == consonants2