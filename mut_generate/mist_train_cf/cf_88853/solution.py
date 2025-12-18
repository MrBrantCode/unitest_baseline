"""
QUESTION:
Write a function called `average_summer_temperature` that takes a list of temperature readings as input, calculates the average monthly temperature in Fahrenheit for the months of June, July, and August, excluding any temperature readings below 80 degrees and above 90 degrees, and returns the rounded average temperature to the nearest whole number. The input list represents temperature readings for each month, with the first element corresponding to June, the second to July, and the third to August.
"""

def average_summer_temperature(temperatures):
    """
    Calculate the average monthly temperature in Fahrenheit for the months of June, July, and August,
    excluding any temperature readings below 80 degrees and above 90 degrees, and returns the rounded average temperature to the nearest whole number.
    
    Parameters:
    temperatures (list): A list of temperature readings for each month, with the first element corresponding to June, the second to July, and the third to August.
    
    Returns:
    int: The rounded average temperature to the nearest whole number.
    """
    
    # Filter out any temperature readings below 80 degrees and above 90 degrees
    filtered_temperatures = [temp for temp in temperatures if 80 <= temp <= 90]
    
    # Calculate the average temperature
    average_temperature = sum(filtered_temperatures) / len(filtered_temperatures)
    
    # Round the average temperature to the nearest whole number
    rounded_average_temperature = round(average_temperature)
    
    return rounded_average_temperature