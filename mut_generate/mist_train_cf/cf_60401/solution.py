"""
QUESTION:
Write a function named `enhanced_words_string` that takes two parameters: a string `s` and a target word `target`. The function should split the input string into words (considering both commas and spaces as delimiters), remove all occurrences of the target word, reverse the remaining words, filter out words longer than 6 characters, and return the resulting list in alphabetical order.
"""

def enhanced_words_string(s, target):
    # Remove the target word, split the string into words
    words = s.replace(target, '').replace(',', ' ').split()
    # Reverse each word and filter out words that are longer than 6 characters
    words = [word[::-1] for word in words if len(word) <= 6]
    # Sort the list of words
    words.sort()
    return words