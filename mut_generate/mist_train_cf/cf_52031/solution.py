"""
QUESTION:
Write a function called `find_isograms` that takes a sentence as input, splits it into individual words, and returns a list of words that are isograms (i.e., words where every letter appears only once). The function should be case-sensitive and should not remove any punctuation or special characters from the words.
"""

def find_isograms(sentence):
    def is_isogram(word):
        return len(word) == len(set(word))

    return [word for word in sentence.split() if is_isogram(word)]