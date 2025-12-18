"""
QUESTION:
Write a function `parse_music` that takes a string of musical notes represented as ASCII characters and returns a list of integers representing the duration of each note in beats. The function should use the following mapping:
- 'o' represents a whole note lasting 4 beats
- 'o|' represents a half note lasting 2 beats
- '.|' represents a quarter note lasting 1 beat

The input string will contain these note characters separated by spaces.
"""

from typing import List

def parse_music(music_string: str) -> List[int]:
    notes_map = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    notes = music_string.split()
    beats = [notes_map[note] for note in notes]
    return beats