"""
QUESTION:
Write a function `count_vowels_and_consonants` that takes a string as input and returns a tuple of two integers representing the number of unique vowels and consonants in the string. The function should be case sensitive and ignore non-alphabet characters. It should count each vowel and consonant only once, even if it appears multiple times in the string.
"""

def count_vowels_and_consonants(s):
    vowels = set("aeiou")
    unique_vowels = set()
    unique_consonants = set()

    for char in s:
        if char.isalpha():
            if char.lower() in vowels:
                unique_vowels.add(char.lower())
            else:
                unique_consonants.add(char.lower())

    return len(unique_vowels), len(unique_consonants)