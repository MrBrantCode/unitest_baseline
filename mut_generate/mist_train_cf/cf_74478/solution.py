"""
QUESTION:
Write a function `vowel_frequency` that takes a string `s` as input and returns a dictionary where the keys are the vowels 'a', 'e', 'i', 'o', 'u' and the values are the frequency of each vowel in the string. The function should be case-insensitive and ignore any non-alphabet characters.
"""

def vowel_frequency(s):
    s = s.lower()
    vowels = 'aeiou'
    result = {i: 0 for i in vowels}

    for char in s:
        if char in vowels:
            result[char] += 1

    return result