"""
QUESTION:
Write a function `count_vowels` that takes a string as input and returns the count of vowel phonemes (both upper and lower case) in the string, ignoring non-alphabetic symbols.
"""

def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count