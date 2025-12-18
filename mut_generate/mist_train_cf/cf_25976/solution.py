"""
QUESTION:
Design a function named `detect_spike_pattern` that takes in a one-dimensional array of EEG data and returns a list representing the spike pattern. The function should identify spikes as peaks in the power spectrum of the EEG data that exceed the mean plus one standard deviation, and the spike pattern should be constructed from the differences between consecutive spike indices.
"""

def detect_spike_pattern(eeg_data):
    # Compute power spectrum of the EEG data
    power_spectra = np.abs(np.fft.rfft(eeg_data))
    # Detect spikes by finding peaks in the power spectrum
    spikes = np.where(power_spectra > np.mean(power_spectra) + np.std(power_spectra))[0]
    # Construct the spike pattern using differences between consecutive spikes
    pattern = [spikes[i+1] - spikes[i] for i in range(len(spikes)-1)]
    return pattern