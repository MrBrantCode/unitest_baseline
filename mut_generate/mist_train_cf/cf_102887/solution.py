"""
QUESTION:
Write a function `find_longest_word_with_vowel` that takes a string as input and returns the longest word that starts with a vowel. The function should be case-insensitive when checking for vowels. If there are multiple words with the same maximum length that start with a vowel, return any of them.
"""

def find_longest_word_with_vowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = string.split()
    longest_word = ''
    for word in words:
        if word[0].lower() in vowels and len(word) > len(longest_word):
            longest_word = word
    return longest_word