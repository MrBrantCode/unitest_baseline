"""
QUESTION:
Create a function called `complex_waveform` that generates a complex waveform as a series of chirps. The function should take in four parameters: `frequencies`, `durations`, `amplitudes`, and `rhythm`, which are lists of frequencies, durations, amplitudes, and intervals of the chirps respectively. The function should also take in a fifth parameter `bird_species`, which is a list of dictionaries containing the characteristics of the bird species associated with each chirp, including 'frequency' and 'duration'. 

The function should generate each chirp with the frequency and duration of the corresponding bird species, and add it to the waveform at the specified interval. The function should return the generated waveform. The sampling rate is assumed to be 44.1 kHz.
"""

import numpy as np

def complex_waveform(frequencies, durations, amplitudes, rhythm, bird_species):
    # Calculate the total duration of the waveform
    duration = sum(durations)

    # Create an array to hold the waveform
    waveform = np.zeros(int(duration * 44100))

    # Calculate the time points to sample at
    t = np.linspace(0, duration, int(duration * 44100), endpoint=False)

    # Calculate the index of the start of each chirp
    start_indices = np.cumsum(np.round(rhythm * 44100).astype(int))

    # Generate each chirp and add it to the waveform
    for i, (f, d, a) in enumerate(zip(frequencies, durations, amplitudes)):
        # Get the bird species and its characteristics
        species = bird_species[i]
        bird_freq = species['frequency']
        bird_dur = species['duration']

        # Generate the chirp signal
        chirp_signal = np.sin(2 * np.pi * bird_freq * np.linspace(0, bird_dur, int(bird_dur * 44100), endpoint=False))

        # Calculate the indices for the current chirp
        start_index = start_indices[i]
        end_index = start_index + len(chirp_signal)

        # Add the chirp to the waveform
        waveform[start_index:end_index] += a * chirp_signal

    return waveform