"""
QUESTION:
Implement a function `parse_music(music_string: str, tempo_multiplier: int = 1)` that takes a string of musical notes and an optional tempo multiplier, and returns a dictionary with note representations as keys, and a tuple of the original note duration and modified duration as values, along with the total number of measures. The note durations are represented by 'o' for a whole note (1), 'o|' for a half note (0.5), and '.|' for a quarter note (0.25). The function should validate that the total beats in a measure do not exceed 1 and split the measure if necessary. The tempo multiplier is used to calculate the modified duration.
"""

from typing import Tuple, Dict

def parse_music(music_string: str, tempo_multiplier: int = 1) -> Tuple[Dict[str, Tuple[float, float]], int]: 
    notes_dict = {'o': 1.0, 'o|': 0.5, '.|': 0.25}

    result_dict = {}
    beats_count = 0
    measure_count = 1

    for note in music_string.split():
        note_duration = notes_dict[note]
        modified_duration = note_duration / tempo_multiplier

        if (beats_count + note_duration) > 1:
            measure_count += 1
            beats_count = note_duration
        else:
            beats_count += note_duration

        if note in result_dict:
            original, modified = result_dict[note]
            result_dict[note] = (original + note_duration, modified + modified_duration)
        else:
            result_dict[note] = (note_duration, modified_duration)
            
    return result_dict, measure_count