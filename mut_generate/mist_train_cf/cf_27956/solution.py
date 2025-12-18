"""
QUESTION:
Implement a function `psd_from_fft2` that calculates the Power Spectral Density (PSD) from a given 2D Fast Fourier Transform (FFT) array. The function should take a 2D FFT array `fft2`, a sampling frequency `fs`, and an optional weight array `weight` as input and return the frequency array `freq_array` and the corresponding PSD array `psd_array`. The frequency array should be generated using `np.fft.fftfreq` and the PSD values should be calculated by squaring the absolute values of the FFT coefficients and normalizing by the product of the FFT size and the sampling frequency. If a weight array is provided, it should be applied to the PSD values by multiplying the squared absolute values of the weight.
"""

import numpy as np

def psd_from_fft2(fft2, fs, weight=None):
    """ 
    Calculate the Power Spectral Density (PSD) from a 2D Fast Fourier Transform (FFT) array.

    Args:
    fft2 (ndarray): 2D array containing the FFT coefficients.
    fs (float): Sampling frequency of the input signal.
    weight (ndarray, optional): Weight array to apply to the PSD calculation. Defaults to None.

    Returns:
    freq_array (ndarray): Array of frequencies corresponding to the PSD values.
    psd_array (ndarray): Power Spectral Density values corresponding to the frequency array.
    """ 
    N = fft2.shape[0]
    freq_array = np.fft.fftfreq(N, 1 / fs)
    psd_array = np.abs(fft2)**2 / (N * fs)
    if weight is not None:
        psd_array *= np.abs(weight)**2
    return freq_array, psd_array