"""
QUESTION:
Write a function `reverse_phrase(phrase)` that takes a string phrase as input and returns a new string where the order of the words is reversed, the order of the characters in each word is reversed, and the first letter of each word is capitalized.
"""

def reverse_phrase(phrase):
    words = phrase.split()
    reversed_words = [word[::-1] for word in reversed(words)]
    capitalized_words = [word.capitalize() for word in reversed_words]
    reversed_phrase = " ".join(capitalized_words)
    return reversed_phrase