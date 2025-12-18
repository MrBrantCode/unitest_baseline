"""
QUESTION:
Design a function `place_wind_turbine` that determines the optimal placement of a wind turbine based on multiple criteria. The function should take in six parameters: wind speed (`V`), wind direction (`Dir`), temperature (`Temp`), humidity (`H`), terrain (`Terrain`), and surrounding environment (`E`). The function should return "Wind turbine placed successfully!" if all conditions are met, otherwise it should return an error message indicating the unsuitable condition. The conditions are as follows:

- Wind speed (`V`) should be greater than or equal to 12 m/s.
- Wind direction (`Dir`) should be between 225 and 315 degrees.
- Temperature (`Temp`) should be between 5 and 30 degrees Celsius, and humidity (`H`) should be between 30 and 80 percent.
- Terrain (`Terrain`) should be either "flat" or "hilly", and surrounding environment (`E`) should be "rural".
"""

def place_wind_turbine(V, Dir, Temp, H, Terrain, E):
    """
    This function determines the optimal placement of a wind turbine based on multiple criteria.

    Parameters:
    V (float): Wind speed in m/s
    Dir (int): Wind direction in degrees
    Temp (int): Temperature in Celsius
    H (int): Relative humidity in percent
    Terrain (str): Type of terrain (options: flat, hilly)
    E (str): Surrounding environment (options: rural)

    Returns:
    str: "Wind turbine placed successfully!" if all conditions are met, otherwise an error message
    """

    # Check wind speed
    if V < 12:
        return "Unable to place wind turbine due to insufficient wind speed."

    # Check wind direction
    if not 225 <= Dir <= 315:
        return "Unable to place wind turbine due to unsuitable wind direction."

    # Check temperature and humidity
    if not (5 <= Temp <= 30 and 30 <= H <= 80):
        return "Unable to place wind turbine due to unsuitable temperature or humidity."

    # Check terrain and surrounding environment
    if not ((Terrain == "flat" or Terrain == "hilly") and E == "rural"):
        return "Unable to place wind turbine due to unsuitable terrain or surrounding environment."

    # Place wind turbine
    return "Wind turbine placed successfully!"