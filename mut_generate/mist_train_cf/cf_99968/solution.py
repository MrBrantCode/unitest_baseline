"""
QUESTION:
Generate all possible chords from a given musical scale, where each chord consists of three notes. The scale is represented as a list of note names. Write a function `generate_chords` that takes the list of note names as input and returns a list of all possible chords, with each chord represented as a list of three note names.
"""

import itertools

def generate_chords(scale_notes):
    """
    Generate all possible chords from a given musical scale.

    Args:
        scale_notes (list): A list of note names.

    Returns:
        list: A list of all possible chords, with each chord represented as a list of three note names.
    """
    # Generate all possible combinations of 3 notes from the scale
    return [list(combination) for combination in itertools.combinations(scale_notes, 3)]