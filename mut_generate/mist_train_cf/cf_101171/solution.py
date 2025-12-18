"""
QUESTION:
Write a function called `count_vowels_and_consonants` that takes a string `s` as input and returns a tuple of two dictionaries. The first dictionary contains the frequency of each vowel in the string, and the second dictionary contains the frequency of each consonant in the string. The function should be case-insensitive and should ignore non-alphabetic characters.
"""

def count_vowels_and_consonants(s):
    vowels = 'aeiou'
    vowel_freq = {}
    consonant_freq = {}
    for char in s.lower():
        if char in vowels:
            vowel_freq[char] = vowel_freq.get(char, 0) + 1
        elif char.isalpha():
            consonant_freq[char] = consonant_freq.get(char, 0) + 1
    return (vowel_freq, consonant_freq)