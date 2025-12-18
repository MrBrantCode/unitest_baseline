"""
QUESTION:
Write a function `reverse_phrase(phrase)` that takes a string phrase as input, reverses the order of the words in the phrase, reverses the order of the characters in each word, and capitalizes the first letter of each word. The function should handle hyphenated or multi-word proper nouns correctly and return the resulting string.
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