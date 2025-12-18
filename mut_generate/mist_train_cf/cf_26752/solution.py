"""
QUESTION:
Implement a function `midi_to_freq` that takes an integer MIDI note number as input and returns the corresponding frequency as a float using the formula `f = 2^((n-69)/12) * 440`, where `n` is the MIDI note number and `f` is the corresponding frequency in Hertz. The function should return -1 if the input is not a valid MIDI note number (i.e., not an integer or outside the range 0-127).
"""

def midi_to_freq(note_number):
    if not isinstance(note_number, int) or note_number < 0 or note_number > 127:
        return -1
    else:
        frequency = 2 ** ((note_number - 69) / 12) * 440
        return frequency