"""
QUESTION:
Implement the function `scale(root_note, scale_mode, num_octaves=1)` that generates a list of notes for the specified scale. The function takes in a root note (`root_note`), a scale mode (`scale_mode`), and the number of octaves (`num_octaves`) as parameters. The function should return a list of notes that form the specified scale based on the given root note, scale mode, and number of octaves. The intervals for different scale modes are: 
- major: [0, 2, 4, 5, 7, 9, 11]
- minor: [0, 2, 3, 5, 7, 8, 10]
- dorian: [0, 2, 3, 5, 7, 9, 10]
The notes in a single octave are: ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"].
"""

def generate_scale(root_note, scale_mode, num_octaves=1):
    intervals = {
        "major": [0, 2, 4, 5, 7, 9, 11],
        "minor": [0, 2, 3, 5, 7, 8, 10],
        "dorian": [0, 2, 3, 5, 7, 9, 10]
    }

    notes_in_octave = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    root_index = notes_in_octave.index(root_note)

    result = []

    for octave in range(num_octaves):
        for interval in intervals[scale_mode]:
            note_index = (root_index + interval) % len(notes_in_octave)
            result.append(notes_in_octave[note_index])
        root_index += len(notes_in_octave)

    return result