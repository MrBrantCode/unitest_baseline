"""
QUESTION:
Create a function `filter_ngrams` that takes a string `text`, an integer `n` representing the size of n-grams, and an integer `k` representing the number of top frequent n-grams to keep. The function should split the input string into words, generate n-grams, and filter out the n-grams that are not among the top k frequent n-grams. The function should return a string of the filtered n-grams.
"""

def filter_ngrams(text, n, k, ngram_frequency):
    # Split text into words
    words = text.split()
    # Generate n-grams
    ngrams = [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]
    # Filter n-grams based on frequency
    top_k_ngrams = sorted(ngram_frequency, key=ngram_frequency.get, reverse=True)[:k]
    # Keep only n-grams in top k frequent n-grams
    filtered_ngrams = [ngram for ngram in ngrams if ngram in top_k_ngrams]
    return ' '.join(filtered_ngrams)