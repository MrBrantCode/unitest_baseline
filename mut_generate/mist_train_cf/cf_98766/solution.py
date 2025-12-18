"""
QUESTION:
Create a function `find_pattern` that takes two parameters: a DNA sequence and a pattern of nucleotides (A, T, C, G). The function should return a list of starting positions of the pattern within the DNA sequence. The function should be able to handle long DNA sequences.
"""

def find_pattern(sequence, pattern):
    locations = []
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i+len(pattern)] == pattern:
            locations.append(i)
    return locations