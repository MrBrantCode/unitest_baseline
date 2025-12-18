"""
QUESTION:
Calculate the angular distance between two celestial objects on the sky given their right ascension (ra) and declination (dec) coordinates using the spherical law of cosines formula. The formula is cos(d) = sin(dec1) * sin(dec2) + cos(dec1) * cos(dec2) * cos(ra2 - ra1), where d is the angular distance between the two points and dec1, dec2, ra1, and ra2 are the declinations and right ascensions in radians.

Implement the function `angularDistance(ra1, dec1, ra2, dec2)` that takes ra1, dec1, ra2, and dec2 in degrees, calculates the angular distance in radians, and returns it.
"""

import math

def angularDistance(ra1: float, dec1: float, ra2: float, dec2: float) -> float:
    # Convert degrees to radians
    ra1_rad = math.radians(ra1)
    dec1_rad = math.radians(dec1)
    ra2_rad = math.radians(ra2)
    dec2_rad = math.radians(dec2)
    
    # Calculate the angular distance using the spherical law of cosines formula
    cos_d = math.sin(dec1_rad) * math.sin(dec2_rad) + math.cos(dec1_rad) * math.cos(dec2_rad) * math.cos(ra2_rad - ra1_rad)
    
    # Ensure the value is within the valid range for cosine
    cos_d = min(1, max(-1, cos_d))
    
    # Calculate the angular distance in radians
    angular_distance = math.acos(cos_d)
    
    return angular_distance