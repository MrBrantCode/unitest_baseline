"""
QUESTION:
Write a function `find_longest_word` that takes a list of words as input and returns the longest word that starts with a vowel, contains at least one consonant, has an even number of characters, and does not contain any duplicate letters. If no word meets these criteria, return an empty string.
"""

def find_longest_word(words):
    longest_word = ""
    
    for word in words:
        if word[0] in "aeiouAEIOU" and any(char not in "aeiouAEIOU" for char in word) and len(word) % 2 == 0 and len(set(word)) == len(word):
            if len(word) > len(longest_word):
                longest_word = word
    
    return longest_word