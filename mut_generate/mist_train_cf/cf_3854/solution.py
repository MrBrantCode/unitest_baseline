"""
QUESTION:
Create a function named `calculate_average_temperature` that takes two lists `days` and `temps` as input. The function should return the average temperature for the last five weekdays, excluding public holidays and outliers. An outlier is defined as a temperature that is more than 2 standard deviations away from the mean temperature. If there are no weekdays (excluding public holidays) in the last five days, the function should return None.
"""

import statistics

def calculate_average_temperature(days, temps):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    non_holiday_weekdays = [weekday for weekday in weekdays if weekday not in days]

    if len(non_holiday_weekdays) < 5:
        return None

    temperatures = [temp for day, temp in zip(days, temps) if day in non_holiday_weekdays]
    if len(temperatures) < 5:
        return None

    mean_temp = statistics.mean(temperatures)
    std_dev = statistics.stdev(temperatures)
    upper_limit = mean_temp + 2 * std_dev
    lower_limit = mean_temp - 2 * std_dev

    filtered_temperatures = [temp for temp in temperatures if lower_limit <= temp <= upper_limit]

    return statistics.mean(filtered_temperatures)