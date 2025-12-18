"""
QUESTION:
Implement a function `generate_pcm_data` that generates PCM audio data based on the given parameters. The function should take three parameters: `numCh`, an integer representing the number of audio channels; `peakLevel`, a floating-point number representing the peak level of the audio signal in decibels (dB); and `sampWidth`, an integer representing the sample width in bits. The function should return the PCM data as a binary string. Assume a sample rate of 44100 Hz and a 1-second duration. The PCM data should be packed into little-endian format according to the specified sample width.
"""

import math
import struct

def generate_pcm_data(numCh, peakLevel, sampWidth):
    freq1 = 440  # Frequency of the first sine wave component (e.g., A4 note)
    freq2 = 660  # Frequency of the second sine wave component (e.g., E5 note)
    fade = 0.5   # Amplitude fade factor
    sampRate = 44100  # Sample rate in Hz
    phase = 0    # Phase offset

    pcm_data = b''  # Initialize PCM data as a binary string

    for i in range(sampRate):  # Iterate over 1 second of audio data
        level = 10 ** (peakLevel / 20)  # Convert peak level from dB to linear scale

        # Calculate the PCM sample value based on the given parameters
        sample = int((fade * level * (0.5 * math.sin((freq1 * 2 * math.pi * i) / sampRate + phase) +
                                       0.5 * math.sin((freq2 * 2 * math.pi * i) / sampRate + phase))))

        # Pack the sample value into little-endian format and append to the PCM data
        pcm_data += struct.pack('<' + ('h' if sampWidth == 16 else 'B'), sample)

    return pcm_data * numCh