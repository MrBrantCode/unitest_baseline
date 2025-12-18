"""
QUESTION:
Write a function `calculate_reaction_rate(jfac, eta, c1, c2, WS1D, tau1, tau2, y, target, rho0, m_x, Jvals)` that takes the following parameters: a scaling factor `jfac`, a coefficient `eta`, coefficients arrays `c1` and `c2`, an instance of a class with a method `calcws1d` `WS1D`, input arrays `tau1`, `tau2`, and `y`, a target index `target`, constants `rho0` and `m_x`, and an array of J values `Jvals`. The function should return the calculated reaction rate in the unit "keV^-1 kg^-1 day^-1", ensuring that the result is within the range [0, 1e30].
"""

import numpy as np

def entrance(jfac, eta, c1, c2, WS1D, tau1, tau2, y, target, rho0, m_x, Jvals):
    R_S1D = jfac / 3.0 * eta * (c1[4] * c2[3] - c1[7] * c2[8])
    rate = R_S1D * np.vectorize(WS1D.calcws1d)(tau1, tau2, y, target)

    conv = (rho0 / 2.0 / np.pi / m_x) * 1.69612985e14  # 1 GeV^-4 * cm^-3 * km^-1 * s * c^6 * hbar^2 to keV^-1 kg^-1 day^-1

    rate = np.clip(rate, 0, 1e30)
    return (4 * np.pi / (2 * Jvals[target] + 1)) * rate * conv