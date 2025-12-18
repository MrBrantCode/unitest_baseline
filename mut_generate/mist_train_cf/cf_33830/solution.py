"""
QUESTION:
Create a function `calculate_topocentric_distance` that calculates the topocentric distance between an observer on Earth and a celestial object. The function should take four parameters: `observer_lat`, `observer_lon`, `celestial_ra`, and `celestial_dec`, representing the observer's latitude and longitude, and the celestial object's right ascension and declination, respectively, all in degrees.

The function should use the formula `cos(d) = sin(δ) * sin(φ) + cos(δ) * cos(φ) * cos(H)` and `r = R * arccos(cos(d))` to calculate the topocentric distance, where `δ` is the declination of the celestial object, `φ` is the observer's latitude, `H` is the hour angle of the celestial object, and `R` is the mean distance of the celestial object from the Earth, which is assumed to be 149.6 million km. The Earth's mean radius is assumed to be 6371 km.
"""

import math

def calculate_topocentric_distance(observer_lat, observer_lon, celestial_ra, celestial_dec):
    observer_lat_rad = math.radians(observer_lat)
    celestial_dec_rad = math.radians(celestial_dec)
    celestial_ra_rad = math.radians(celestial_ra)
    observer_lon_rad = math.radians(observer_lon)

    phi = observer_lat_rad
    delta = celestial_dec_rad
    H = observer_lon_rad - celestial_ra_rad

    cos_d = math.sin(delta) * math.sin(phi) + math.cos(delta) * math.cos(phi) * math.cos(H)
    topocentric_distance = 149.6 * 10**6 * math.acos(cos_d) / 6371

    return topocentric_distance