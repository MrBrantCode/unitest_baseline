"""
QUESTION:
Implement the `singleQubitDecayCalculate` function, which calculates the excited state population at each step of a qubit's evolution and stores it in the `populations` dictionary. The function should take three parameters: `qub`, `state`, and `i`, where `i` represents the current step. The `populations` dictionary has two keys: 'excitedAnalytical' and 'excitedNumerical', to store the analytical and numerical excited state populations, respectively. The analytical excited state population is given by the formula: `P(t) = 0.5 * e^(-(0.00001 * (decayRateSM + 1) * 2 + 1j) * 50 * t)`, where `t` is the time at each step, calculated as `i * qub.stepSize`.
"""

import numpy as np

def singleQubitDecayCalculate(qub, state, i, decayRateSM):
    excitedPopulation = 0.5 * np.exp(-(0.00001 * (decayRateSM + 1) * 2 + 1j) * 50 * (i * qub.stepSize))
    return excitedPopulation