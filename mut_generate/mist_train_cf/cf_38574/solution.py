"""
QUESTION:
Implement the function `freq_to_notes(freqs)` where `freqs` is a list of frequencies. The function should return a string representing the note names corresponding to the input frequencies based on the standard musical scale with the following frequency ranges: 
- "C" : 16.35 - 17.32 Hz
- "C#" : 17.32 - 18.35 Hz
- "D" : 18.35 - 19.45 Hz
- "D#" : 19.45 - 20.60 Hz
- "E" : 20.60 - 21.83 Hz
- "F" : 21.83 - 23.12 Hz
- "F#" : 23.12 - 24.50 Hz
- "G" : 24.50 - 25.96 Hz
- "G#" : 25.96 - 27.50 Hz
- "A" : 27.50 - 29.14 Hz
- "A#" : 29.14 - 30.87 Hz
- "B" : 30.87 - 32.70 Hz
If a frequency does not correspond to any note in the standard musical scale, it should be represented as "Unknown" in the output string. The output string should contain the note names separated by a space and should not have any leading or trailing spaces.
"""

def freq_to_notes(freqs):
    note_ranges = {
        "C": (16.35, 17.32),
        "C#": (17.32, 18.35),
        "D": (18.35, 19.45),
        "D#": (19.45, 20.60),
        "E": (20.60, 21.83),
        "F": (21.83, 23.12),
        "F#": (23.12, 24.50),
        "G": (24.50, 25.96),
        "G#": (25.96, 27.50),
        "A": (27.50, 29.14),
        "A#": (29.14, 30.87),
        "B": (30.87, 32.70)
    }

    notes = ""
    for f in freqs:
        note_found = False
        for note, (lower, upper) in note_ranges.items():
            if lower <= f <= upper:
                notes += note + " "
                note_found = True
                break
        if not note_found:
            notes += "Unknown "
    return notes.strip()