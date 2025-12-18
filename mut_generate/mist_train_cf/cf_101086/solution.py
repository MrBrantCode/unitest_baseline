"""
QUESTION:
Write a function `find_pattern(sequence, pattern)` that takes a DNA sequence and a pattern of nucleotides as input and returns a list of the starting positions of the pattern within the sequence. The function should be able to handle long sequences.
"""

def find_pattern(sequence, pattern):
    locations = []
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i+len(pattern)] == pattern:
            locations.append(i)
    return locations