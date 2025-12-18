"""
QUESTION:
Write a function named `count_letter_frequency` that takes a string of lowercase letters and spaces as input and returns the frequency of each letter in the string, excluding any vowels. The function should be case-sensitive.
"""

def count_letter_frequency(string):
    letter_freq = {}
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for char in string:
        if char.isalpha() and char.lower() not in vowels:
            letter_freq[char] = letter_freq.get(char, 0) + 1
    return letter_freq