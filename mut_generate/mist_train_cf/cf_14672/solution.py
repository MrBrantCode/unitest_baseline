"""
QUESTION:
Write a function `generate_ngrams(string, gram_size)` that takes a string of words and an integer `gram_size` as input, and returns a list of strings representing the n-grams of the input string. Each n-gram should consist of `gram_size` consecutive words from the original string, and the function should return all possible n-grams.
"""

def generate_ngrams(string, gram_size):
    words = string.split()
    ngrams = []
    
    for i in range(len(words) - gram_size + 1):
        ngram = " ".join(words[i:i+gram_size])
        ngrams.append(ngram)
    
    return ngrams