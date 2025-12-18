"""
QUESTION:
Write a function `count_vowels_in_words` that takes a string as input and returns a list of integers representing the number of vowels in each word in the string, where the string is converted to lowercase and non-alphanumeric characters are ignored.
"""

def count_vowels_in_words(s):
    return [sum(1 for char in word if char in 'aeiou') for word in s.lower().split()]