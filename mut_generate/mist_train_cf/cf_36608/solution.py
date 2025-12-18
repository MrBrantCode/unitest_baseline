"""
QUESTION:
Create a Python function `generate_dummy_spec` that takes in parameters `wave`, `npix`, `s2n`, and `seed` to generate a dummy spectral data specification. The `wave` parameter is an optional array of wavelengths (default `None`), `npix` is the number of pixels in the spectral data, `s2n` is the signal-to-noise ratio of the spectral data, and `seed` is an optional integer for the random seed (default `None`). 

The function should return a dictionary containing the spectral data specification with keys `wave`, `npix`, `s2n`, and `seed`. If `wave` is not provided, generate a default array of wavelengths based on `npix`.
"""

import numpy as np

def generate_dummy_spec(wave=None, npix=2000, s2n=10.0, seed=None):
    if wave is None:
        wave = np.linspace(4000, 7000, npix)  

    dummy_spec = {
        'wave': wave,
        'npix': npix,
        's2n': s2n,
        'seed': seed
    }

    return dummy_spec