"""
QUESTION:
Write a function named `count_vowels_and_consonants` that takes a string as input and returns a tuple containing two integers: the number of unique vowels and the number of unique consonants in the string. The function should be case-insensitive and only count alphabetic characters.
"""

def count_vowels_and_consonants(string):
    string = string.lower()
    vowel_count = 0
    consonant_count = 0
    unique_vowels = set()
    unique_consonants = set()

    for char in string:
        if char.isalpha():
            if char in "aeiou":
                if char not in unique_vowels:
                    vowel_count += 1
                    unique_vowels.add(char)
            else:
                if char not in unique_consonants:
                    consonant_count += 1
                    unique_consonants.add(char)

    return vowel_count, consonant_count