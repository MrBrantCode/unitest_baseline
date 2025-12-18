"""
QUESTION:
Implement a function `temperature_analysis` that takes 9 dictionaries (`eq_lib3`, `eq_lib3T1`, `eq_lib3T2`, `eq_lib3_t`, `eq_lib3_tt`, `eq_lib3T1_t`, `eq_lib3T2_t`, `eq_lib2T`, `eq_lib2`) as input, where each dictionary contains temperature data as a NumPy array under the key `temperature`. The function should return a tuple of two boolean values. The first value should indicate whether any of the temperature data contains NaN values. The second value should indicate whether the temperature data from `eq_lib2T` is close to the temperature data from `eq_lib2` and whether the temperature data from `eq_lib3T1` is close to the temperature data from `eq_lib3` (with a transposed array for `eq_lib3T1`).
"""

import numpy as np

def temperature_analysis(eq_lib3, eq_lib3T1, eq_lib3T2, eq_lib3_t, eq_lib3_tt, eq_lib3T1_t, eq_lib3T2_t, eq_lib2T, eq_lib2):
    # Check for NaN values
    nan_check = any([
        np.any(np.isnan(eq_lib3['temperature'])),
        np.any(np.isnan(eq_lib3T1['temperature'])),
        np.any(np.isnan(eq_lib3T2['temperature'])),
        np.any(np.isnan(eq_lib3_t['temperature'])),
        np.any(np.isnan(eq_lib3_tt['temperature'])),
        np.any(np.isnan(eq_lib3T1_t['temperature'])),
        np.any(np.isnan(eq_lib3T2_t['temperature']))
    ])

    # Compare temperature data using assert_allclose
    temp_comparison = np.allclose(eq_lib2T['temperature'].T, eq_lib2['temperature']) and \
                     np.allclose(np.swapaxes(eq_lib3T1['temperature'], 0, 1), eq_lib3['temperature'])

    return nan_check, temp_comparison