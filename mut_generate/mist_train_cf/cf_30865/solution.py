"""
QUESTION:
Implement a function `generate_dft_matrix(N: int) -> np.ndarray` that takes an integer `N` as input and returns the corresponding Discrete Fourier Transform (DFT) matrix of size `N x N` as a NumPy array, where each element `D[j, k]` is defined as `1/sqrt(N) * e^(-2*pi*i*j*k/N)`, with `j` and `k` ranging from 0 to `N-1`.
"""

import numpy as np

def generate_dft_matrix(N: int) -> np.ndarray:
    D = np.zeros((N, N), dtype=np.complex128)
    for j in range(N):
        for k in range(N):
            D[j, k] = 1 / np.sqrt(N) * np.exp(-2j * np.pi * j * k / N)
    return D