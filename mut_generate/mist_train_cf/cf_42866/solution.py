"""
QUESTION:
Implement a function `load_buf(buf, frequency)` that fills the given buffer `buf` with audio samples based on the provided `frequency`. The function should use a predefined number of audio samples `N_SAMPLES`, a sample rate `SAMPLE_RATE`, a period size `PERIOD_SIZE`, and an array of audio wave samples `wave` to calculate and load the buffer. The function should return the filled buffer. 

Note that the variables `N_SAMPLES`, `SAMPLE_RATE`, `PERIOD_SIZE`, and `wave` are predefined and will be provided. The function should only take `buf` and `frequency` as input.
"""

def load_buf(buf, frequency):
    """
    Fills the given buffer with audio samples based on the provided frequency.

    Parameters:
    buf (list): The buffer to be filled with audio samples.
    frequency (int): The frequency of the audio signal.

    Returns:
    list: The filled buffer.
    """
    step = N_SAMPLES * frequency // SAMPLE_RATE
    for i in range(0, PERIOD_SIZE):
        buf[i] = wave[(step * i * N_SAMPLES // PERIOD_SIZE) % N_SAMPLES]
    return buf