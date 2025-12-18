"""
QUESTION:
Write a function named `count_vowels(s)` that takes a string `s` as input and returns the number of vowels in the string, ignoring case, punctuation marks, and special characters. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string. Assume the input string will be in English.
"""

def count_vowels(s):
    s = s.lower()
    vowel_count = 0
    for c in s:
        if c in 'aeiou':
            vowel_count += 1
    return vowel_count