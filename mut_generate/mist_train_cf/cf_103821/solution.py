"""
QUESTION:
Write a function `filter_vowel_words` that takes a string as input and returns a list of words, excluding any words that start with a vowel (both lowercase and uppercase). The function should consider the first character of each word to check for vowels.
"""

def filter_vowel_words(my_string):
    return [word for word in my_string.split() if not word[0].lower() in 'aeiou']