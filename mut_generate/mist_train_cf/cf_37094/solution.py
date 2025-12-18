"""
QUESTION:
Implement a function `calc_diss_energy_fd(tau, strs)` that calculates the dissipation energy based on two input NumPy arrays `tau` and `strs`. The dissipation energy is calculated using the formula: 

\[ \text{dissipation energy} = \sum_{i=1}^{n} \left| \frac{1}{2} \cdot (strs[i] - strs[i-1]) \cdot (tau[i] - tau[i-1]) \right| \]

Where `n` is the length of the input arrays `tau` and `strs`. The function should return the total dissipation energy value.
"""

import numpy as np

def calc_diss_energy_fd(tau, strs):
    # Calculate the differences in tau and strs arrays
    delta_tau = np.diff(tau)
    delta_strs = np.diff(strs)
    
    # Calculate the dissipation energy using the formula
    diss_energy = np.abs(0.5 * delta_strs * delta_tau)
    
    # Sum the dissipation energy values to get the total dissipation energy
    total_diss_energy = np.sum(diss_energy)
    
    return total_diss_energy