"""
QUESTION:
Write a function `count_vowels_and_consonants(s)` that takes a string `s` as input and returns a tuple containing the count of vowels and consonants in the string. The function should consider only the English alphabetic characters and ignore case sensitivity. Non-alphabetic characters and characters from non-Latin alphabets should be excluded from the count.
"""

def count_vowels_and_consonants(s):
    vowels_count = 0
    consonants_count = 0

    for char in s.lower():
        if char.isalpha():
            if char in 'aeiou':
                vowels_count += 1
            else:
                consonants_count += 1

    return vowels_count, consonants_count