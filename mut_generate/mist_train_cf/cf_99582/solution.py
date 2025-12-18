"""
QUESTION:
Write a Python function `find_pattern(sequence, pattern)` that takes two parameters: a DNA sequence (a string consisting of the characters A, T, C, and G) and a pattern (a substring of the DNA sequence). The function should return a list of the starting positions of the pattern within the sequence.
"""

def find_pattern(sequence, pattern):
    locations = []
    for i in range(len(sequence) - len(pattern) + 1):
        if sequence[i:i+len(pattern)] == pattern:
            locations.append(i)
    return locations