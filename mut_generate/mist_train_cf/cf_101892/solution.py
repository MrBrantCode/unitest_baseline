"""
QUESTION:
Generate all possible chords from a given musical scale. 

Create a function `generate_chords` that takes a list of notes representing a musical scale as input and returns all possible chords consisting of three notes. The function should not assume any specific musical mode or key. 

Restrictions: 
- Each chord must consist of exactly three notes.
- No chord can contain duplicate notes.
- The order of the notes in each chord does not matter.
"""

import itertools

def generate_chords(scale_notes):
    """
    Generate all possible chords from a given musical scale.

    Args:
        scale_notes (list): A list of notes representing a musical scale.

    Returns:
        list: A list of lists, where each sublist is a chord consisting of three unique notes.
    """
    # Generate all possible combinations of 3 notes from the scale
    chords = list(itertools.combinations(scale_notes, 3))
    return chords