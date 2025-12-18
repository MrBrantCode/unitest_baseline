"""
QUESTION:
Implement a Python function `calculate_dft` that takes an input signal `x` and returns the discrete Fourier transform (DFT) coefficients `X` using the formula: 
\[ X[k] = \sum_{n=0}^{N-1} x[n] \cdot e^{-i 2 \pi \frac{kn}{N}} \]
where `N` is the total number of samples in the input signal `x` and `k` ranges from 0 to `N-1`.
"""

import numpy as np

def calculate_dft(x):
    N = len(x)
    X = []
    for k in range(N):
        X_k = 0
        for n in range(N):
            X_k += x[n] * np.exp(-1j * 2 * np.pi * k * n / N)
        X.append(X_k)
    return X