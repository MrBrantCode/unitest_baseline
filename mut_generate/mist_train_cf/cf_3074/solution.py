"""
QUESTION:
Create a function named `longest_word` that takes a sentence as input and returns the longest word, excluding punctuation marks, that starts with a capital letter and contains at least one vowel. If multiple words have the same length, return the word that occurs first in the sentence. If no words meet these conditions, return an empty string.
"""

def longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if word[0].isupper() and any(char in "aeiouAEIOU" for char in word):
            word = word.strip(",.-!?")
            if len(word) > len(longest):
                longest = word
    return longest