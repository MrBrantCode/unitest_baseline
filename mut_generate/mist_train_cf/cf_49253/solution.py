"""
QUESTION:
Implement a function called `phrase_sorter` that sorts a list of phrases based on the number of words in each phrase. If two phrases have the same number of words, sort them in alphabetical order based on the first word of each phrase.
"""

def phrase_sorter(phrases):
    # Use a lambda function to count the number of words in each phrase
    phrases_sorted = sorted(phrases, key=lambda phrase: (len(phrase.split(" ")), phrase.split(" ")[0]))
    return phrases_sorted