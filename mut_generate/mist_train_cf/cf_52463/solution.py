"""
QUESTION:
Write a function `generate_ngrams(text, n=3)` that generates n-grams of the given text with a specified window size `n`. The function should split the text into words and return a list of strings where each string is a sequence of `n` consecutive words from the text.
"""

def generate_ngrams(text, n=3):
    words = text.split(' ')
    ngrams = zip(*[words[i:] for i in range(n)])
    return [' '.join(ngram) for ngram in ngrams]