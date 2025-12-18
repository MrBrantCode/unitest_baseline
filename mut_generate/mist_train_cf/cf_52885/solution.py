"""
QUESTION:
Write a function `find_th_words` that takes a sentence as input and returns a list of words that start with the character set "th" (case-insensitive). The input sentence may contain punctuation.
"""

def find_th_words(sentence):
    sentence = sentence.replace('.', '')
    words = sentence.split()
    matched_words = [word for word in words if word.lower().startswith('th')]
    return matched_words