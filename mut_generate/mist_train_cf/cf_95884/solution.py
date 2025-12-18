"""
QUESTION:
Create a function `calculate_average_temperature` that takes a list of dictionaries, where each dictionary contains a "month" and a "temperature", and returns the average temperature in Fahrenheit for the months of June, July, and August, excluding any temperature readings below 80 degrees. The function should round the average temperature to the nearest whole number. The input list will contain at least one temperature reading for each month, and the "month" will be a string and the "temperature" will be a number.
"""

def calculate_average_temperature(temperature_data):
    """
    Calculate the average temperature in Fahrenheit for the months of June, July, and August, 
    excluding any temperature readings below 80 degrees.

    Args:
        temperature_data (list): A list of dictionaries, where each dictionary contains a "month" and a "temperature".

    Returns:
        int: The rounded average temperature.
    """
    # Filter temperature readings for June, July, and August
    temperature_readings = [data["temperature"] for data in temperature_data 
                            if data["month"] in ["June", "July", "August"] and data["temperature"] >= 80]
    
    # Calculate the average temperature
    average_temperature = sum(temperature_readings) / len(temperature_readings)
    
    # Round the average temperature to the nearest whole number
    rounded_average_temperature = round(average_temperature)
    
    return rounded_average_temperature