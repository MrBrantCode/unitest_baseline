"""
QUESTION:
Write a function `count_vowels` that takes a string as input and returns the number of vowels present, considering consecutive vowels as one. The function should ignore case and non-alphabet characters.
"""

def count_vowels(s):
    s = s.lower()
    vowels = set('aeiou')
    count = 0
    in_vowel = False
    for char in s:
        if char in vowels and not in_vowel:
            count += 1
            in_vowel = True
        elif char not in vowels:
            in_vowel = False
    return count