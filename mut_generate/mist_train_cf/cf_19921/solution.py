"""
QUESTION:
Write a function named `calculate_average_temperature` that takes a list of dictionaries `temperature_data` as input, where each dictionary contains a month and its corresponding temperature in Fahrenheit. The function should calculate the average temperature for the months of June, July, and August, excluding any temperature readings below 80 degrees, and return the rounded average temperature to the nearest whole number.
"""

def calculate_average_temperature(temperature_data):
    # Create an array to store temperature readings
    temperature_readings = [data["temperature"] for data in temperature_data 
                            if data["month"] in ["June", "July", "August"] and data["temperature"] >= 80]
    
    # Calculate the average temperature
    average_temperature = sum(temperature_readings) / len(temperature_readings) if temperature_readings else 0
    
    # Round the average temperature to the nearest whole number
    rounded_average_temperature = round(average_temperature)
    
    return rounded_average_temperature