"""
QUESTION:
Implement a function `tf2linphase(h, normalize=True)` that takes a 1D NumPy array `h` representing a transfer function and an optional boolean parameter `normalize` (defaulting to `True`), and returns a new 1D NumPy array containing the linear phase transfer function. The function should calculate the length of the transfer function array, perform a Fast Fourier Transform on the array, modify the phase of the frequency response to make it linear, perform an inverse FFT, and consider the optional `normalize` parameter.
"""

import numpy as np

def tf2linphase(h, normalize=True):
    """Converts a transfer function to linear phase

    Parameters
    ----------
    h : ndarray
        Numpy array containing the original transfer function
    normalize : bool, optional
        Flag to indicate whether to normalize the linear phase transfer function (default is True)

    Returns
    -------
    h_lin : ndarray
        Numpy array containing the linear phase transfer function
    """
    N = len(h)
    H = np.fft.fft(h)

    # Modify the phase of the frequency response to make it linear
    phase = np.linspace(0, np.pi, N, endpoint=False) if normalize else np.zeros(N)
    H_lin = np.abs(H) * np.exp(1j * phase)

    # Perform an inverse FFT to obtain the linear phase transfer function
    h_lin = np.fft.ifft(H_lin)

    return h_lin