"""
QUESTION:
Generate a list of unique n-grams from a given sentence. The `generate_ngrams` function should take two parameters: a string `sentence` of length between 1 and 10^6, and an integer `gram_size` between 2 and 10. The function should return a list of all unique n-grams of size `gram_size` in the given `sentence`, in the order they appear, excluding punctuation marks. If the given `gram_size` is greater than the number of words in the sentence, the function should return an empty list. The time complexity should be O(n) and the space complexity should be O(m), where n is the length of the input string and m is the number of unique n-grams generated.
"""

import re

def generate_ngrams(sentence, gram_size):
    """
    Generate a list of unique n-grams from a given sentence.

    Args:
    sentence (str): The input sentence.
    gram_size (int): The size of the n-grams.

    Returns:
    list: A list of unique n-grams in the order they appear.

    """
    # Remove punctuation marks and split the sentence into words
    words = re.sub(r'[^\w\s]', '', sentence).split()

    # If the number of words is less than gram_size, return an empty list
    if len(words) < gram_size:
        return []

    # Initialize a set to store unique n-grams
    ngrams = set()

    # Generate n-grams
    for i in range(len(words) - gram_size + 1):
        ngram = ' '.join(words[i:i + gram_size])
        ngrams.add(ngram)

    # Return the list of unique n-grams in the order they appear
    seen = set()
    result = []
    for i in range(len(words) - gram_size + 1):
        ngram = ' '.join(words[i:i + gram_size])
        if ngram not in seen:
            result.append(ngram)
            seen.add(ngram)

    return result