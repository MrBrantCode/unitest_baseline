"""
QUESTION:
Create a function named `parse_music` that takes a string of musical notes represented as ASCII characters and returns a list of integers representing the duration of each note in beats. The notes and their corresponding beat values are as follows: 'o' equals 4 beats, 'o|' equals 2 beats, and '.|' equals 1 beat. The input string is space-separated, and the function should return the list of beat values in the same order as the notes in the input string.
"""

from typing import List

def parse_music(music_string: str) -> List[int]:    
    beat_values = {}
    beat_values['o'] = 4
    beat_values['o|'] = 2
    beat_values['.|'] = 1
    
    return [beat_values[note] for note in music_string.split()]