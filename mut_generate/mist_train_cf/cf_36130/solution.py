"""
QUESTION:
Write a function `generate_song(notes: List[Tuple[float, float]]) -> str` that takes a list of tuples representing notes and their start times. Each tuple contains a note length (in seconds) and the start time (in seconds) for the note. The function should generate a song by inserting the notes at the specified start times and return a string indicating the completion of the song generation process. The function should handle the case where the song generation process is interrupted by a KeyboardInterrupt, in which case it should return 'Song generation interrupted'.
"""

from typing import List, Tuple

def generate_song(notes: List[Tuple[float, float]]) -> str:
    song = ""
    try:
        for note_length, start in notes:
            song = song[:int(start)] + "note" + song[int(start):]
    except KeyboardInterrupt:
        return 'Song generation interrupted'
    return 'Song generation completed'