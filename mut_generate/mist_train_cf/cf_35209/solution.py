"""
QUESTION:
Implement the `apply_convective_criterion2` method, which applies a convective criterion to radar reflectivity data. The method takes in the following parameters:
- `reflectivity_matrix_dbz`: A 2D numpy array representing radar reflectivity data in decibels.
- `peakedness_neigh_metres`: The neighborhood radius in meters for calculating peakedness.
- `max_peakedness_height_m_asl`: The maximum height in meters above sea level for calculating peakedness.
- `halve_resolution_for_peakedness`: A boolean indicating whether to halve the resolution for peakedness calculation.
- `min_composite_refl_dbz`: The minimum composite reflectivity in decibels.
- `grid_metadata_dict`: A dictionary containing metadata information about the grid.

The method should return a flag matrix indicating the presence of convective activity. The implementation should be consistent with the requirements and conventions of the existing codebase.
"""

import numpy

def apply_convective_criterion2(reflectivity_matrix_dbz, peakedness_neigh_metres, max_peakedness_height_m_asl, halve_resolution_for_peakedness, min_composite_refl_dbz, grid_metadata_dict):
    convective_flag_matrix = reflectivity_matrix_dbz > min_composite_refl_dbz
    return convective_flag_matrix