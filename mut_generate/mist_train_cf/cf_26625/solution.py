"""
QUESTION:
Write a function `extract_features(data, N_trials, N_chans, N_class, n_harmonicas, val_chans, N_pos, n_features)` that takes the following parameters: 
- `data`: a 3D numpy array of shape (N_samples, N_chans, N_trials) representing the EEG data for all trials and channels.
- `N_trials`: an integer representing the number of EEG trials.
- `N_chans`: an integer representing the number of EEG channels.
- `N_class`: an integer representing the number of classes in the EEG data.
- `n_harmonicas`: an integer representing the number of harmonics to consider in the feature extraction process.
- `val_chans`: a 1D numpy array representing the valid channels for feature extraction.
- `N_pos`: a 1D numpy array representing the positions for feature extraction.
- `n_features`: an integer representing the number of features to extract.

The function should return four feature matrices, each as a numpy array of shape (N_trials, N_chans * N_class * n_harmonicas), after calculating the Fast Fourier Transform (FFT) of the EEG data for each trial and channel, and populating the feature matrices accordingly.
"""

import numpy as np

def extract_features(data, N_trials, N_chans, N_class, n_harmonicas, val_chans, N_pos, n_features):
    F_dez = np.zeros((N_trials, N_chans * N_class * n_harmonicas))
    F_onze = np.zeros((N_trials, N_chans * N_class * n_harmonicas))
    F_doze = np.zeros((N_trials, N_chans * N_class * n_harmonicas))
    F_treze = np.zeros((N_trials, N_chans * N_class * n_harmonicas))

    for trial in range(N_trials):
        Chans_XY = 0
        for chans in val_chans - 1:
            a = abs(np.fft.fft(data[:, chans, trial]))  
            b = abs(np.fft.fft(data[:, chans, trial]))  
            c = abs(np.fft.fft(data[:, chans, trial]))  
            d = abs(np.fft.fft(data[:, chans, trial]))  

            F_dez[trial, Chans_XY + np.array(range(n_features))] = a[N_pos[range(n_features)]]
            F_onze[trial, Chans_XY + np.array(range(n_features))] = b[N_pos[range(n_features)]]
            F_doze[trial, Chans_XY + np.array(range(n_features))] = c[N_pos[range(n_features)]]
            F_treze[trial, Chans_XY + np.array(range(n_features))] = d[N_pos[range(n_features)]]

    return F_dez, F_onze, F_doze, F_treze