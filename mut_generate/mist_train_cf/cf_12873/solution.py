"""
QUESTION:
Write a function `join_vowel_words_reversed` that takes a list of strings as input. The function should concatenate the strings that start with a vowel (case-insensitive) using a pipe (|) as a separator, and then reverse the resulting string.
"""

def join_vowel_words_reversed(words):
    vowel_words = [word for word in words if word[0].lower() in ['a', 'e', 'i', 'o', 'u']]
    joined_string = '|'.join(vowel_words)
    reversed_string = joined_string[::-1]
    return reversed_string