"""
QUESTION:
Write a function named `generate_chords` that takes a list of notes representing a musical scale and returns all possible chords consisting of three notes. The function should not take any other parameters and should return a list of chords where each chord is a list of three notes.
"""

import itertools

def generate_chords(scale_notes):
    """
    Generate all possible chords consisting of three notes from a given musical scale.
    
    Parameters:
    scale_notes (list): A list of notes representing a musical scale.
    
    Returns:
    list: A list of chords where each chord is a list of three notes.
    """
    # Generate all possible combinations of 3 notes from the scale
    return [list(combination) for combination in itertools.combinations(scale_notes, 3)]