"""
QUESTION:
Create a function `count_nucleotide_patterns(dna_sequence, patterns)` that takes a DNA sequence as a string and a list of nucleotide patterns as strings. The function should return a dictionary where the keys are the input patterns and the values are the counts of occurrences of each pattern within the DNA sequence. The function should be able to handle large DNA sequences efficiently.
"""

def count_nucleotide_patterns(dna_sequence, patterns):
    pattern_counts = {pattern: 0 for pattern in patterns}
    sequence_length = len(dna_sequence)
    
    for pattern in patterns:
        pattern_length = len(pattern)
        for i in range(sequence_length - pattern_length + 1):
            if dna_sequence[i:i+pattern_length] == pattern:
                pattern_counts[pattern] += 1
    
    return pattern_counts