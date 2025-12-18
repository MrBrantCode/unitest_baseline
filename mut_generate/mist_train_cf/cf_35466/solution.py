"""
QUESTION:
Implement the function `interpolate_values(coordinates, values, target_coords, power)` that takes a list of geographical coordinates and their corresponding values, and returns a smoothed interpolation of the values using the Inverse Distance Weighting (IDW) method. 

The function should accept the following parameters:
- `coordinates`: a list of tuples representing the geographical coordinates of the input values.
- `values`: a list of numerical values corresponding to the coordinates.
- `target_coords`: a list of tuples representing the geographical coordinates where the interpolation is to be performed.
- `power`: a numerical value representing the power parameter for the IDW method.

The function should return a list of interpolated values corresponding to the `target_coords` using the IDW method.
"""

import numpy as np

def interpolate_values(coordinates, values, target_coords, power):
    interpolated_values = []
    for target_coord in target_coords:
        numerator = 0
        denominator = 0
        for i in range(len(coordinates)):
            distance = np.sqrt((target_coord[0] - coordinates[i][0])**2 + (target_coord[1] - coordinates[i][1])**2)
            if distance == 0:
                interpolated_values.append(values[i])
                break
            weight = 1 / distance**power
            numerator += values[i] * weight
            denominator += weight
        if denominator != 0:
            interpolated_values.append(numerator / denominator)
    return interpolated_values