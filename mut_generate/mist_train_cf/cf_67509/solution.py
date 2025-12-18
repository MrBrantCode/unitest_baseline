"""
QUESTION:
Write a function named `ParseMusic` that takes two parameters: `music_string` and `BPM`. `BPM` should be between 0 and 300. The function should parse `music_string` into notes, calculate the transpose value for each note, and return the list of transpose values. The transpose value is calculated as `70 + BPM / 10 * beats_per_note`, where `beats_per_note` is 4 for 'o', 2 for 'o|', and 1 for '.|'.
"""

def ParseMusic(music_string, BPM):
    if not (0 <= BPM <= 300):
        raise Exception("BPM should be between 0 and 300")

    notes = music_string.split()
    transposed_notes = []
    beats_per_note = {'o': 4, 'o|': 2, '.|': 1}

    for note in notes:
        transpose_val = 70 + BPM // 10 * beats_per_note[note]
        transposed_notes.append(transpose_val)

    return transposed_notes