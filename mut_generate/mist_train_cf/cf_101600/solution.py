"""
QUESTION:
Create a function called `reverse_phrase` that takes a string as input and returns a string. The function should reverse the order of the words in the phrase, reverse the order of the characters in each word, and capitalize the first letter of each word, regardless of whether the original phrase contains hyphenated or multi-word proper nouns.
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