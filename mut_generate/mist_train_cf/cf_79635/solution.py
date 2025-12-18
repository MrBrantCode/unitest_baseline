"""
QUESTION:
The function `calculate_distance(N, E, D, A)` should calculate the straight-line distance from a drone's current position to its point of origin after a sequence of movements. The drone first moves northeast by N km, then due east by E km, and finally by D km in a direction A degrees from north. The calculation should account for the Earth's curvature using the Haversine formula. The function should be able to handle varying inputs for N, E, D, and A. The Earth's radius is approximately 6371 km. The input A is in degrees and represents the direction of the third movement (0 degrees is north, 90 degrees is east, 180 degrees is south, 270 degrees is west).
"""

import math

def entrance(N, E, D, A):
    A = math.radians(A) # Convert to radians
    R = 6371  # radius of Earth in km

    # Start point
    lat1, lon1 = 0, 0  

    # NE displacement
    x, y = math.sin(math.pi/4) * N, math.cos(math.pi/4) * N
    # Add E displacement
    x += E

    # Polar to Cartesian
    lat2 = math.degrees(y / R)
    lon2 = math.degrees(x / (R * math.cos(math.radians(lat2))))
  
    # Direction rule
    x = D * math.sin(A)
    y = D * math.cos(A)

    lat3 = lat2 + math.degrees(y / R)
    lon3 = lon2 + math.degrees(x / (R * math.cos(math.radians(lat3))))

    # Haversine formula
    lat1, lon1, lat2, lon2 = math.radians(lat1), math.radians(lon1), math.radians(lat3), math.radians(lon3)
    dlat, dlon = lat2 - lat1, lon2 - lon1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c