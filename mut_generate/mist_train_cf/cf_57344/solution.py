"""
QUESTION:
Write a function `unmatched_subseqs(listA, listB)` that takes two lists of strings as input and returns a list of strings from `listB` that are not a subsequence of any string in `listA`. A string `B` is a subsequence of `A` if it can be derived from `A` by deleting some characters without changing the order of the remaining characters. The comparison must be case sensitive. If a same string is present multiple times in `listB`, and if it is a subsequence of any string in `listA`, it should be considered as a successful match for each of its instances. The function should be efficient in terms of time and space complexity to handle large inputs.
"""

from functools import reduce

def is_subseq(seq1, seq2):
    it = iter(seq2)
    return all(char in it for char in seq1)

def unmatched_subseqs(listA, listB):
    unmatched = []
    for seqB in listB:
        if not any(is_subseq(seqB, seqA) for seqA in listA):
            unmatched.append(seqB)
    return unmatched