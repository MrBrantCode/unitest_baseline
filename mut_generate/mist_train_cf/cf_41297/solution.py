"""
QUESTION:
Implement the `average_pf_change_during_repairs(system_model)` function, which calculates the average change in the performance factor (`pf`) of the system components during repairs. The `system_model` contains a 2D numpy array `system_pf` representing the performance factor of the system components over time. Return the average change in performance factor during repairs.
"""

import numpy as np

def average_pf_change_during_repairs(system_model):
    t, pf = np.vstack(system_model.system_pf).T
    unique_mask = np.diff(t) == 1
    delta_pf = np.diff(pf)[unique_mask]
    average_change = np.mean(delta_pf)
    return average_change