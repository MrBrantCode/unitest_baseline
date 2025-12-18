"""
QUESTION:
Write a function `total_distance(x, y, t)` to compute the total distance two spaceships would have covered after `t` hours, considering the speed of light is approximately 300,000 km/s. 

The function should accept the following parameters:
- `x`: a floating point number representing the speed of the first spaceship as a percentage of the speed of light. (0 < x < 1)
- `y`: a floating point number representing the speed of the second spaceship as a percentage of the speed of light. (0 < y < 1)
- `t`: an integer representing time in hours.

Return the total distance covered by both spaceships from the perspective of a stationary observer, accurate to the nearest kilometer.
"""

def total_distance(x, y, t):
    light_speed_km_hr = 300000 * 3600   # speed of light in km/hr
    return round((x * light_speed_km_hr * t + y * light_speed_km_hr * t))