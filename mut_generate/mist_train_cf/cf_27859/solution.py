"""
QUESTION:
Implement the `load_horiz` function to read data from a file with comma-separated time, yaw, pitch, roll, north, east, and down values, and perform linear interpolation for these flight parameters based on the given time points. The function should handle cases where the requested interpolation time is outside the range of the recorded time points in the file by using the nearest available time points. The interpolated values should be stored in the `yaw_interp`, `pitch_interp`, `roll_interp`, `north_interp`, `east_interp`, and `down_interp` variables.
"""

import numpy as np

def load_horiz(filename):
    data = np.genfromtxt(filename, delimiter=',')
    time_points = data[:, 0]
    yaw_values = data[:, 1]
    pitch_values = data[:, 2]
    roll_values = data[:, 3]
    north_values = data[:, 4]
    east_values = data[:, 5]
    down_values = data[:, 6]

    def interpolate(time, values):
        return np.interp(time, time_points, values)

    yaw_interp = interpolate(time_points, yaw_values)
    pitch_interp = interpolate(time_points, pitch_values)
    roll_interp = interpolate(time_points, roll_values)
    north_interp = interpolate(time_points, north_values)
    east_interp = interpolate(time_points, east_values)
    down_interp = interpolate(time_points, down_values)
    return yaw_interp, pitch_interp, roll_interp, north_interp, east_interp, down_interp