"""
QUESTION:
Write a function called generate_sound_waveform that generates and returns a 1-second sound waveform with a specified frequency and amplitude. The waveform should be represented as a list of floating point numbers, with each number representing the amplitude of the sound at a particular point in time. The function should take two parameters: frequency (in Hz) and amplitude (as a float between 0 and 1). The function should also take an optional parameter, sample_rate, which defaults to 44100 (the standard sample rate for CD quality audio).
"""

def generate_sound_waveform(frequency, amplitude, sample_rate=44100):
    """
    Generates a 1-second sound waveform with a specified frequency and amplitude.

    Args:
        frequency (int): Frequency of the sound in Hz.
        amplitude (float): Amplitude of the sound, as a float between 0 and 1.
        sample_rate (int, optional): Sample rate of the sound. Defaults to 44100.

    Returns:
        list: A list of floating point numbers representing the sound waveform.
    """

    # Calculate the total number of samples in the waveform
    num_samples = sample_rate
    
    # Generate the waveform
    waveform = [amplitude * (1 + (1 - 2 * (i % 2))) * (1 - abs(2 * (i % (sample_rate // frequency)) / (sample_rate // frequency) - 1)) for i in range(num_samples)]
    
    return waveform