"""
QUESTION:
Create a function named `parse_music` that takes a string of space-separated musical notes ('o', 'o|', '.|') and returns a list of integers representing the beat duration of each note. The conversion rules are as follows: 'o' equals 4 beats, 'o|' equals 2 beats, and '.|' equals 1 beat.
"""

from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')
    beat_duration = []
    for note in notes:
        if note == 'o':
            beat_duration.append(4)
        elif note == 'o|':
            beat_duration.append(2)
        elif note == '.|':
            beat_duration.append(1)
    return beat_duration