"""
QUESTION:
Write a function `count_distinct_vowels(string)` that takes a string of up to 100 characters as input and returns the number of distinct vowels, considering both uppercase and lowercase vowels as the same and excluding any vowels that appear more than once consecutively in the string.
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