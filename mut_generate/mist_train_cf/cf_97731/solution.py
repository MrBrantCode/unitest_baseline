"""
QUESTION:
Generate all possible chords of 3 notes from a given musical scale. 

Function name: Not specified, but for clarity, let's call it `generate_chords`. 

The function should take a list of notes as input, where each note is a string, and return a list of all possible chords, where each chord is a list of 3 notes.

Restrictions: The order of the notes in each chord does not matter, and no note should be repeated in a chord.
"""

import itertools

def generate_chords(scale_notes):
    """
    Generate all possible chords of 3 notes from a given musical scale.
    
    Args:
    scale_notes (list): A list of notes in the musical scale.
    
    Returns:
    list: A list of all possible chords, where each chord is a list of 3 notes.
    """
    return list(itertools.combinations(scale_notes, 3))