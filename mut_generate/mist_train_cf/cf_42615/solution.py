"""
QUESTION:
Given two 1D arrays `tbs` and `tas`, write a function `process_arrays(tbs, tas)` that reshapes these arrays into 3D arrays, with each 3D array having dimensions determined by splitting into multiple 2D arrays with 5 rows and 20 columns, and then scale the values by dividing by 100.0. The function should return the reshaped and scaled 3D arrays `tbs_3d` and `tas_3d`. The input arrays should have a length that is a multiple of 100 to ensure even reshaping.
"""

import numpy as np

def entrance(tbs, tas):
    tbs_3d = np.array(tbs).reshape(len(tbs) // 100, 5, 20) / 100.0
    tas_3d = np.array(tas).reshape(len(tas) // 100, 5, 20) / 100.0
    return tbs_3d, tas_3d