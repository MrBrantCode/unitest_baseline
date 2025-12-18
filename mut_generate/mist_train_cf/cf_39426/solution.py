"""
QUESTION:
Implement a Python function `Fourier_approx(N, t, T, A)` that approximates a square wave using a Fourier series given the number of terms in the series `N`, the time array `t`, the period of the square wave `T`, and the amplitude `A`. The function should return the Fourier series approximation of the square wave, calculated using the formula `f(t) = (4*A/π) * ∑[1/n * sin(2*π*n*t/T)]` for odd terms from 1 to `N`.
"""

import numpy as np

def Fourier_approx(N, t, T, A):
    f = np.zeros_like(t)
    for n in range(1, N+1, 2):  # Sum over odd terms
        f += (4*A/np.pi) * (1/n) * np.sin(2*np.pi*n*t/T)
    return f