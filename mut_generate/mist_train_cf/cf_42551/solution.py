"""
QUESTION:
Create a function `apply_calibration_parameters(raw_measurements, misalignmentsAndScales, biases)` that takes a 3x1 NumPy array `raw_measurements`, a 3x3 NumPy array `misalignmentsAndScales` representing misalignments and scales for the sensor axes, and a 3x1 NumPy array `biases` representing biases for the sensor outputs, and returns the calibrated sensor outputs after applying the misalignments, scales, and biases.

The function should perform the following steps: 
1. Apply the misalignments and scales to the raw sensor measurements by multiplying `misalignmentsAndScales` with `raw_measurements`.
2. Add the biases to the results obtained in step 1.

The function should return the calibrated sensor outputs as a 3x1 NumPy array.
"""

import numpy as np

def entance(raw_measurements, misalignmentsAndScales, biases):
    # Apply misalignments and scales
    calibrated_measurements = np.dot(misalignmentsAndScales, raw_measurements)

    # Add biases
    calibrated_measurements += biases

    return calibrated_measurements