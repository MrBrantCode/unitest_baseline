"""
QUESTION:
Write a function `find_pattern_positions(seq: str, w: int, pattern: str) -> List[int]` that finds the starting positions of all occurrences of a specific pattern within a DNA sequence. The function takes a DNA sequence `seq` containing only 'A', 'C', 'G', and 'T' with a length between 1 and 10^6, a pattern length `w` between 1 and the length of `seq`, and a pattern string. It returns a list of 0-indexed starting positions where the pattern is found in the DNA sequence. If the pattern is not found, return an empty list.
"""

from typing import List

def find_pattern_positions(seq: str, w: int, pattern: str) -> List[int]:
    positions = []
    for i in range(len(seq) - w + 1):
        if seq[i:i+w] == pattern:
            positions.append(i)
    return positions