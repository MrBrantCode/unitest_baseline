"""
QUESTION:
Write a function called `reverse_phrase` that takes a string `phrase` as input. The function should reverse the order of the words in the phrase, reverse the order of the characters in each word, and capitalize the first letter of each word. The function should return the modified string. The function should work correctly for phrases with hyphenated words and multi-word proper nouns.
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