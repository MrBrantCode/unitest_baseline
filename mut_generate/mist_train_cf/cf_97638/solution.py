"""
QUESTION:
Generate a function `generate_chords` that takes a list of notes as input and returns all possible combinations of three notes as chords. The function should not assume any specific key or mode, and the input list of notes can be any valid musical scale.
"""

import itertools

def generate_chords(notes):
    """
    Generate all possible combinations of three notes as chords from a given list of notes.
    
    Args:
        notes (list): A list of musical notes.
    
    Returns:
        list: A list of all possible combinations of three notes as chords.
    """
    return list(itertools.combinations(notes, 3))