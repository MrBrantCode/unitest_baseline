"""
QUESTION:
Write a function `reverse_phrase(phrase)` that takes a string phrase as input and returns the phrase with the order of the words reversed, the order of the characters in each word reversed, and the first letter of each word capitalized.
"""

def reverse_phrase(phrase):
    # split the phrase into a list of words
    words = phrase.split()
    # reverse the order of the words and reverse the order of the characters in each word
    reversed_words = [word[::-1] for word in reversed(words)]
    # capitalize the first letter of each word
    capitalized_words = [word.capitalize() for word in reversed_words]
    # join the words back together into a string
    reversed_phrase = " ".join(capitalized_words)
    return reversed_phrase