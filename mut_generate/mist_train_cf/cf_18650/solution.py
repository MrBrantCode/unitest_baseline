"""
QUESTION:
Create a function named `calculate_average_temp` that takes two lists as input: `days` and `temps`, where `days` is a list of day names and `temps` is a list of corresponding temperatures. The function should calculate the average temperature for the last five weekdays (Monday to Friday), excluding any temperatures that are more than 2 standard deviations away from the mean temperature. If there are no weekdays in the last five days, the function should return `None`.
"""

import statistics

def calculate_average_temp(days, temps):
    weekday_temps = [temps[i] for i in range(-1, -6, -1) if days[i] in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']]
    
    if len(weekday_temps) == 0:
        return None
    
    mean = statistics.mean(weekday_temps)
    std_dev = statistics.stdev(weekday_temps)
    temps_no_outliers = [temp for temp in weekday_temps if abs(temp - mean) <= 2 * std_dev]
    
    return statistics.mean(temps_no_outliers)