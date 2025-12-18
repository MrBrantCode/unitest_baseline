"""
QUESTION:
Create a function named `calculate_weekly_temperatures` that takes a 2D list of temperature readings for each day of the week and returns a dictionary with the average, median, minimum, maximum, and standard deviation of temperatures for each day, excluding any day with an average temperature outside the range of 0 to 100 degrees Celsius. The function should also sort the dictionary by the median temperature in descending order and return the day with the highest and lowest median temperature. The result should be stored in a dictionary with the day of the week as the key and a nested dictionary containing the temperature data as the value.
"""

import statistics

def calculate_weekly_temperatures(temperature_data):
    """
    This function calculates and returns the average, median, minimum, maximum, 
    and standard deviation of temperatures for each day of the week. It excludes 
    any day with an average temperature outside the range of 0 to 100 degrees Celsius. 
    The function also sorts the result by the median temperature in descending order 
    and returns the day with the highest and lowest median temperature.
    
    Parameters:
    temperature_data (list): A 2D list of temperature readings for each day of the week
    
    Returns:
    dict: A dictionary with the average, median, minimum, maximum, and standard deviation 
          of temperatures for each day, sorted by the median temperature in descending order.
    """
    
    weekly_temperatures = {}
    
    for i, temperatures in enumerate(temperature_data):
        avg_temp = sum(temperatures) / len(temperatures)
        
        if 0 <= avg_temp <= 100:
            median_temp = statistics.median(temperatures)
            min_temp = min(temperatures)
            max_temp = max(temperatures)
            sd_temp = statistics.stdev(temperatures)
            
            daily_temperatures = {
                'average_temperature': avg_temp,
                'median_temperature': median_temp,
                'minimum_temperature': min_temp,
                'maximum_temperature': max_temp,
                'standard_deviation': sd_temp
            }
            
            weekly_temperatures[f'Day {i+1}'] = daily_temperatures
    
    sorted_temperatures = sorted(weekly_temperatures.items(), key=lambda x: x[1]['median_temperature'], reverse=True)
    
    result = {
        'weekly_temperatures': dict(sorted_temperatures),
        'highest_median_day': sorted_temperatures[0][0],
        'lowest_median_day': sorted_temperatures[-1][0]
    }
    
    return result