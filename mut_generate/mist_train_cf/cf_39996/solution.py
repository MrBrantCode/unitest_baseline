"""
QUESTION:
Write a function `validate_ibound(ibound, botm, top, min_thickness, tolerance)` that takes in a 3D ibound array, 3D bottom elevation array `botm`, 3D model topography array `top`, a minimum thickness value `min_thickness`, and a tolerance value `tolerance`. The function should return True if the ibound array meets the following conditions: 
- the cell values at a specific location are based on the presence of valid bottom elevations,
- individual cells with thickness less than a minimum value are not deactivated, unless all cells at the same location have thickness less than the minimum value plus a tolerance,
- cells with NaN values in the model topography result in the exclusion of the highest active bottom elevations at those locations,
- cells with valid topographies are set to inactive (idomain=0) in all layers when all bottom elevations in a specific layer are NaN.

The ibound array represents the boundary conditions for a groundwater model, where each element indicates whether a cell is active (1) or inactive (0). The `~` operator represents the logical NOT operation.
"""

import numpy as np

def validate_ibound(ibound, botm, top, min_thickness, tolerance):
    # Validation 1: Check ibound based on valid bottom elevations
    condition1 = np.array_equal(ibound.astype(bool), ~np.isnan(botm))

    # Calculate layer thicknesses
    thicknesses = np.diff(np.concatenate((botm, top[:, None]), axis=1), axis=1)

    # Validation 2: Check ibound based on layer thickness
    condition2 = np.all((thicknesses >= min_thickness) | (ibound == 0) | (thicknesses < (min_thickness + tolerance)))

    # Validation 3: Check exclusion of highest active bottom elevations at NaN top locations
    condition3 = np.all(ibound[np.isnan(top)] == 0)

    # Validation 4: Check idomain=0 for cells with valid topographies and NaN bottom elevations
    condition4 = np.all(ibound[:, np.all(np.isnan(botm), axis=0)] == 0)

    return condition1 and condition2 and condition3 and condition4