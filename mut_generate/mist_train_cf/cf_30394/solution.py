"""
QUESTION:
Implement a function named `longest_consecutive_subsequence` that takes a non-empty sequence of integers as input and returns the longest subsequence of consecutive integers present in the input sequence. If there are multiple longest consecutive subsequences, return the first one encountered.
"""

import itertools

def longest_consecutive_subsequence(sequence):
    def _consecutives():
        i = 0
        while i < len(sequence):
            subseq = [sequence[i]]
            j = i + 1
            while j < len(sequence) and sequence[j] == subseq[-1] + 1:
                subseq.append(sequence[j])
                j += 1
            yield subseq
            i = j

    return next(itertools.takewhile(lambda t: len(t), _consecutives()))