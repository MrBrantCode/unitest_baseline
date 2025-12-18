"""
QUESTION:
Write a function `find_subsequence(genome_seq, nucleotide_seq)` that determines whether `nucleotide_seq` is a subsequence of `genome_seq`. The function should return `True` if `nucleotide_seq` is a subsequence of `genome_seq` and `False` otherwise. Assume that both `genome_seq` and `nucleotide_seq` are non-empty strings consisting only of the characters 'A', 'C', 'G', and 'T'.
"""

def find_subsequence(genome_seq, nucleotide_seq):
    return nucleotide_seq in genome_seq