"""
QUESTION:
Write a function `reverseComplement` that takes a string `dna` of characters 'A', 'C', 'G', and 'T' as input and returns the reverse complement of the DNA sequence, where 'A' is replaced by 'T', 'T' is replaced by 'A', 'C' is replaced by 'G', and 'G' is replaced by 'C'.
"""

def reverseComplement(dna):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_comp = ''.join(complement[base] for base in reversed(dna))
    return reverse_comp