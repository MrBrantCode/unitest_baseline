"""
QUESTION:
Write a function named `longest_increasing_subsequence` or `common_subsequences` that takes three sequences of integers as input and returns the longest increasing subsequence common to all three sequences. The function should handle negative numbers and zero, and if there are multiple longest increasing subsequences, it should return all of them.
"""

def longest_increasing_subsequence(seq1, seq2, seq3):
    def longest_increasing_subsequence_single(seq):
        for length in range(len(seq), 0, -1):
            for sub in combinations(seq, length):
                if list(sub) == sorted(sub):
                    return set(sub)

    from itertools import combinations
    subsequences = [longest_increasing_subsequence_single(seq) for seq in [seq1, seq2, seq3]]
    return set.intersection(*subsequences)