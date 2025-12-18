"""
QUESTION:
Design a function `place_wind_turbine` that determines the optimal placement of a wind turbine based on multiple criteria. The function should take in the following parameters: wind speed in m/s (`wind_speed`), wind direction in degrees (`wind_direction`), temperature in Celsius (`temperature`), relative humidity in percent (`humidity`), terrain type (`terrain`), and surrounding environment (`environment`). The function should return a string indicating whether the wind turbine can be placed successfully or not. The conditions for successful placement are: wind speed >= 12 m/s, wind direction between 225 and 315 degrees, temperature between 5 and 30 Celsius, humidity between 30 and 80 percent, terrain is either "flat" or "hilly", and environment is "rural".
"""

def place_wind_turbine(wind_speed, wind_direction, temperature, humidity, terrain, environment):
    """
    This function determines the optimal placement of a wind turbine based on multiple criteria.

    Args:
    wind_speed (float): wind speed in m/s
    wind_direction (int): wind direction in degrees
    temperature (float): temperature in Celsius
    humidity (float): relative humidity in percent
    terrain (str): type of terrain (options: flat, hilly, mountainous)
    environment (str): surrounding environment (options: urban, suburban, rural)

    Returns:
    str: A string indicating whether the wind turbine can be placed successfully or not.
    """

    if wind_speed >= 12 and 225 <= wind_direction <= 315 and 5 <= temperature <= 30 and 30 <= humidity <= 80 and terrain in ["flat", "hilly"] and environment == "rural":
        return "Wind turbine placed successfully!"
    else:
        return "Unable to place wind turbine."