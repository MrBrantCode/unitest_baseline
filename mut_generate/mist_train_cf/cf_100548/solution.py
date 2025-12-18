"""
QUESTION:
Write a function `calculate_hours_to_complete_lifecycle(temp, humidity)` that calculates the number of hours an adult mosquito needs to live to complete its life cycle based on the temperature and humidity of its environment, while satisfying the additional requirement that the total time taken for the adult mosquito to feed on blood should not exceed 10 hours. The function should take two parameters: `temp` (the temperature in degrees Celsius) and `humidity` (the relative humidity as a percentage). The lifespan of the mosquito is affected by temperature and humidity, with optimal ranges of 10-40 degrees Celsius and 30-90% relative humidity.
"""

def calculate_hours_to_complete_lifecycle(temp, humidity):
    """
    Calculate the number of hours an adult mosquito needs to live to complete its life cycle based on the temperature and humidity of its environment,
    while satisfying the additional requirement that the total time taken for the adult mosquito to feed on blood should not exceed 10 hours.

    Parameters:
    temp (float): The temperature in degrees Celsius.
    humidity (float): The relative humidity as a percentage.

    Returns:
    int: The number of hours the adult mosquito needs to live to complete its life cycle.
    """
    base_lifespan = 8 * 24  # 8 days in hours
    if temp < 10 or temp > 40:
        lifespan = base_lifespan  # outside of optimal temperature range
    else:
        if temp < 25:
            temp_factor = (temp - 10) / 15
        else:
            temp_factor = (40 - temp) / 15
        if humidity < 30 or humidity > 90:
            lifespan = base_lifespan  # outside of optimal humidity range
        else:
            hum_factor = (humidity - 30) / 60
            lifespan = base_lifespan * (1 + temp_factor + hum_factor)
    feeding_time = min(10, lifespan / 4)  # maximum 25% of lifespan spent feeding
    return int(lifespan - feeding_time)