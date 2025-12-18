"""
QUESTION:
Implement a function `modified_precision(reference, hypothesis, n)` that calculates the modified precision score for a given reference translation and a hypothesis translation up to a specified value of n. The function should consider n-gram matches between the reference and hypothesis translations. The function should take three parameters: `reference`, a list of words representing the reference translation; `hypothesis`, a list of words representing the hypothesis translation; and `n`, an integer representing the maximum n-gram size to consider. The function should return the modified precision score as a float.
"""

from collections import Counter

def modified_precision(reference, hypothesis, n):
    def ngrams(tokens, n):
        return [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]

    reference_ngrams = Counter(ngrams(reference, n))
    hypothesis_ngrams = Counter(ngrams(hypothesis, n))

    clipped_counts = sum(min(hypothesis_ngrams[ngram], reference_ngrams[ngram]) for ngram in hypothesis_ngrams)

    total_hypothesis_ngrams = sum(hypothesis_ngrams.values())

    if total_hypothesis_ngrams == 0:
        return 0.0
    else:
        return clipped_counts / total_hypothesis_ngrams