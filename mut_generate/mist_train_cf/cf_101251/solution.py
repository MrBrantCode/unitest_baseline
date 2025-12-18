"""
QUESTION:
Create a function `count_pattern` that takes a string `dna_sequence` and a string `pattern` as input and returns the number of times the `pattern` repeats in the `dna_sequence`. The `pattern` is "ATCGCGATCGATCGATC" and it must match exactly.
"""

def count_pattern(dna_sequence, pattern):
    """
    Counts the number of times a given pattern repeats in a DNA sequence.
    
    Args:
        dna_sequence (str): The DNA sequence to search in.
        pattern (str): The pattern to search for.
    
    Returns:
        int: The number of times the pattern repeats in the DNA sequence.
    """
    count = 0
    for i in range(len(dna_sequence) - len(pattern) + 1):
        if dna_sequence[i:i+len(pattern)] == pattern:
            count += 1
    return count