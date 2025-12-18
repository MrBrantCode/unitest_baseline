"""
QUESTION:
Create a function called `calculate_weekly_temperatures` that takes a list of lists containing temperature readings for each day of the week as input. The function should calculate the average temperature, median temperature, minimum temperature, maximum temperature, and standard deviation of temperature for each day. The function should store these results in a dictionary where each key is a day of the week and the value is another dictionary containing the temperature statistics. The function should exclude any day with an average temperature outside the range of 0 to 100 degrees Celsius. The function should return a sorted dictionary by median temperature in descending order, along with the day with the highest and lowest median temperature.
"""

import statistics

def calculate_weekly_temperatures(temperature_data):
    # Initialize the main dictionary
    weekly_temperatures = {}

    # Loop through each day's temperature data
    for i, temperatures in enumerate(temperature_data):
        # Calculate average temperature
        avg_temp = sum(temperatures) / len(temperatures)
        
        # Exclude any day with an average temperature outside the range of 0 to 100 degrees Celsius
        if 0 <= avg_temp <= 100:
            # Calculate median temperature
            median_temp = statistics.median(temperatures)
            
            # Calculate minimum temperature
            min_temp = min(temperatures)
            
            # Calculate maximum temperature
            max_temp = max(temperatures)
            
            # Calculate standard deviation of temperature
            sd_temp = statistics.stdev(temperatures)
            
            # Create a nested dictionary with all the temperature data
            daily_temperatures = {
                'average_temperature': avg_temp,
                'median_temperature': median_temp,
                'minimum_temperature': min_temp,
                'maximum_temperature': max_temp,
                'standard_deviation': sd_temp
            }
            
            # Add the nested dictionary to the main dictionary using the day of the week as the key
            weekly_temperatures[f'Day {i+1}'] = daily_temperatures
    
    # Sort the dictionary by the median temperature in descending order
    sorted_temperatures = sorted(weekly_temperatures.items(), key=lambda x: x[1]['median_temperature'], reverse=True)

    # Return the sorted dictionary along with the day with the highest and lowest median temperature
    return dict(sorted_temperatures), sorted_temperatures[0][0], sorted_temperatures[-1][0]