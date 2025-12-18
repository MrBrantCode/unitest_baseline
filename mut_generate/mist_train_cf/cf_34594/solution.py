"""
QUESTION:
Implement a Python function `propIR` that simulates the propagation of a wave through a medium using the Fresnel diffraction integral. The function should take the following parameters: `u` (the input wavefront), `step` (the spatial step size), `L` (the size of the observation plane), `wavel` (the wavelength of the wave), and `z` (the propagation distance). It should return the output wavefront `u(x', y')` based on the input wavefront `u(x, y)` and the specified propagation distance `z`. The Fresnel diffraction integral formula is defined as `u(x', y') = (e^(ikz) / (i * λ * z)) * ∫∫[u(x, y) * e^(-(ik/2z)((x-x')^2 + (y-y')^2))] dx dy`.
"""

import numpy as np

def propIR(u, step, L, wavel, z):
    M, N = np.shape(u)
    x = np.linspace(-L/2.0, L/2.0-step, M)
    y = np.linspace(-L/2.0, L/2.0-step, N)
    X, Y = np.meshgrid(x, y)
    
    k = 2 * np.pi / wavel
    u_out = np.zeros_like(u, dtype=np.complex128)
    
    for i in range(M):
        for j in range(N):
            integral = np.sum(np.sum(u * np.exp(-1j * k / (2 * z) * ((X - x[i])**2 + (Y - y[j])**2)))) * step**2
            u_out[i, j] = (np.exp(1j * k * z) / (1j * wavel * z)) * integral
    
    return u_out