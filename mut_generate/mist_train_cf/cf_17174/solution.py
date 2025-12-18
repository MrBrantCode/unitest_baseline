"""
QUESTION:
Write a function named `count_distinct_vowels` that takes a string as input and returns the number of distinct vowels in the string, considering both uppercase and lowercase vowels as the same and excluding any vowels that appear more than once consecutively. The input string will contain at most 100 characters.
"""

def count_distinct_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    distinct_vowels = set()
    prev_vowel = None

    for char in string.lower():
        if char in vowels:
            if char != prev_vowel:
                distinct_vowels.add(char)
            prev_vowel = char

    return len(distinct_vowels)