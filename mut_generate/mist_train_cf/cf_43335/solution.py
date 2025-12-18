"""
QUESTION:
Create a function `create_augmented_settings` that takes a dictionary of signal processing blocks as input, where each key is a string representing the name of the block and each value is a list of signal processing class instances. The function should return a new dictionary with the same keys as the input dictionary, but with augmented signal processing instances as values. 

The augmented versions should include two versions of each original block: 
- A version with the same parameters as the original block.
- A version with modified parameters:
  - For 'comp-' block: Increase the threshold by 5 dB and keep the ratio unchanged.
  - For 'gain+' block: Reduce the gain by 3 dB.
  - For 'gain-' block: Increase the gain by 3 dB.
  - For 'lpf-' block: Double the cutoff frequency.
  - For 'lpf+' block: Halve the cutoff frequency.
"""

class Compressor:
    def __init__(self, threshold_db, ratio):
        self.threshold_db = threshold_db
        self.ratio = ratio

class Gain:
    def __init__(self, gain_db):
        self.gain_db = gain_db

class LowpassFilter:
    def __init__(self, cutoff_frequency_hz):
        self.cutoff_frequency_hz = cutoff_frequency_hz

def create_augmented_settings(signal_processing_blocks):
    """
    Create augmented versions of signal processing blocks.

    Args:
    signal_processing_blocks (dict): A dictionary of signal processing blocks.
        Each key is a string representing the name of the block, and each value
        is a list of signal processing class instances.

    Returns:
    dict: A dictionary with the same keys as the input dictionary, but with
        augmented signal processing instances as values.
    """
    augmented_settings = {}
    for key, value in signal_processing_blocks.items():
        if key == 'comp-':
            augmented_settings[key] = [Compressor(threshold_db=value[0].threshold_db - 5, ratio=value[0].ratio), Compressor(threshold_db=value[0].threshold_db, ratio=value[0].ratio)]
        elif key == 'gain+':
            augmented_settings[key] = [Gain(gain_db=value[0].gain_db - 3), Gain(gain_db=value[0].gain_db)]
        elif key == 'gain-':
            augmented_settings[key] = [Gain(gain_db=value[0].gain_db + 3), Gain(gain_db=value[0].gain_db)]
        elif key == 'lpf-':
            augmented_settings[key] = [LowpassFilter(cutoff_frequency_hz=value[0].cutoff_frequency_hz * 2), LowpassFilter(cutoff_frequency_hz=value[0].cutoff_frequency_hz)]
        elif key == 'lpf+':
            augmented_settings[key] = [LowpassFilter(cutoff_frequency_hz=value[0].cutoff_frequency_hz / 2), LowpassFilter(cutoff_frequency_hz=value[0].cutoff_frequency_hz)]
    return augmented_settings