"""
QUESTION:
Write a function named `parse_music` that takes two parameters: `music_string` and an optional `tempo_multiplier` with a default value of 1.0. The function should interpret the `music_string` as a sequence of musical notes in a specific ASCII format, where 'o' represents a whole note (1 beat), 'o|' represents a half note (0.5 beats), and '.|' represents a quarter note (0.25 beats). The `tempo_multiplier` should adjust the beats per measure for each note. The function should return a tuple containing a list of fractional values representing the duration of each note in beats per measure, and an integer representing the total number of measures. The cumulative beats in any measure should not exceed 1; if it does, the measure should be divided into multiple measures.
"""

from typing import Tuple, List

def parse_music(music_string: str, tempo_multiplier: float = 1.0) -> Tuple[List[float], int]:
    """
    This function interprets the music_string as a sequence of musical notes in a specific ASCII format,
    where 'o' represents a whole note (1 beat), 'o|' represents a half note (0.5 beats), and '.|' represents a quarter note (0.25 beats).
    The tempo_multiplier adjusts the beats per measure for each note.
    The function returns a tuple containing a list of fractional values representing the duration of each note in beats per measure,
    and an integer representing the total number of measures.
    The cumulative beats in any measure should not exceed 1; if it does, the measure should be divided into multiple measures.
    """
    notes = { 'o': 1.0, 'o|': 0.5, '.|' : 0.25 }
    note_dur = [] #store duration of each note
    measure = 1 #start with 1 measure
    
    #initialize a variable to keep track of the total duration
    total_duration = 0.0

    #iterate over each note in the music
    for note in music_string.split():
        note_duration = notes.get(note) * tempo_multiplier # duration of each note
        note_dur.append(note_duration)
        
        total_duration += note_duration

        #if total_duration surpasses 1, increment measure and reset total_duration
        if total_duration > 1.0:
            measure += 1
            total_duration -= 1.0
    return note_dur, measure