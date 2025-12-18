"""
QUESTION:
Implement a function `sign_speed(east_vel, north_vel, spd, dir_vel, flooddir)` that calculates the signed speed and principal direction of water currents. The function takes in the eastward velocity component `east_vel`, northward velocity component `north_vel`, speed `spd`, principal direction `dir_vel`, and flood direction `flooddir` as inputs. The signed speed should be calculated based on the principal direction using the Polagye Routine. The function should return the signed speed and principal direction. The principal direction is calculated using the arctangent of the northward and eastward velocity components.
"""

import numpy as np

def calculate_signed_speed_and_direction(east_vel, north_vel, spd, dir_vel, flooddir):
    """
    Calculate the signed speed and principal direction of water currents.

    Args:
    east_vel (float): Eastward velocity component.
    north_vel (float): Northward velocity component.
    spd (float): Speed.
    dir_vel (float): Principal direction.
    flooddir (float): Flood direction.

    Returns:
    tuple: Signed speed and principal direction.
    """
    # Calculate signed speed
    s_signed = np.sign(np.cos(np.deg2rad(dir_vel - flooddir))) * spd
    # Calculate principal direction
    PA = np.arctan2(north_vel, east_vel) * 180 / np.pi
    return s_signed, PA