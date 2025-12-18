"""
QUESTION:
Implement a function `calc_wd_mean_radial` that calculates the weighted mean of a set of angles in degrees by converting the angles to unit vectors, computing the mean of the unit vectors, and converting the resulting mean vector back to an angle.

The function takes a 1D numpy array `angles_array_deg` containing angles in degrees and an integer `axis` specifying the axis along which the mean will be calculated (default value is 0). The function returns the weighted mean angle in degrees.

Constraints: The input `angles_array_deg` has at least one element, and the angles are in the range [0, 360).
"""

import numpy as np

def calc_wd_mean_radial(angles_array_deg, axis=0):
    # Use unit vectors to calculate the mean
    wd_x = np.cos(angles_array_deg * np.pi / 180.)
    wd_y = np.sin(angles_array_deg * np.pi / 180.)
    
    # Calculate the mean of the unit vectors
    mean_wd_x = np.mean(wd_x, axis=axis)
    mean_wd_y = np.mean(wd_y, axis=axis)
    
    # Convert the mean vector back to an angle
    mean_angle_rad = np.arctan2(mean_wd_y, mean_wd_x)
    mean_angle_deg = mean_angle_rad * 180. / np.pi
    
    return mean_angle_deg