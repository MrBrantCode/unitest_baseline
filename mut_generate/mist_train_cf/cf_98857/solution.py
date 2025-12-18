"""
QUESTION:
Write a function `count_vowels_and_consonants` that takes a string `s` as input and returns a tuple containing two dictionaries: `vowel_freq` and `consonant_freq`. `vowel_freq` should store the frequency of each vowel in the string and `consonant_freq` should store the frequency of each consonant in the string. Ignore non-alphabetic characters, and consider vowels as 'a', 'e', 'i', 'o', and 'u'. The function should be case-insensitive.
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