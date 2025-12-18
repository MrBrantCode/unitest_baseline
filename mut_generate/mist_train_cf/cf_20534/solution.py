"""
QUESTION:
Create a function named `calculate_dna_weight` that takes a string of nucleotides as input and returns the total weight of the DNA sequence based on the following rules:
- Each nucleotide has a specific weight: A = 1, C = 2, G = 3, T = 4.
- The weight of each nucleotide is doubled if it appears consecutively in the sequence.
- The function should handle sequences of any length, be case-insensitive, ignore invalid characters, and handle sequences containing only A, C, G, and T, as well as those containing other characters.
"""

def calculate_dna_weight(sequence):
    weights = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    prev_nucleotide = None
    weight = 0

    for nucleotide in sequence.upper():
        if nucleotide in weights:
            if nucleotide == prev_nucleotide:
                weight += weights[nucleotide] * 2
            else:
                weight += weights[nucleotide]
            prev_nucleotide = nucleotide

    return weight